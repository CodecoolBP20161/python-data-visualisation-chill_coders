from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Imaging():

    @staticmethod
    def check_space(all_coords, current_coords, word_size):
        OK = True
        for i in range(0, word_size[1]):
            for j in range(0, word_size[0]):
                if not all_coords[current_coords[0]+j][current_coords[1]+i]:
                    OK = False
                    break
        return OK

    @staticmethod
    def toggle_coords(all_coords, current_coords, word_size):
        for i in range(0, word_size[1]):
            for j in range(0, word_size[0]):
                all_coords[current_coords[0]+j][current_coords[1]+i] = False

    @staticmethod
    def get_min_coords(all_coords, current_coords, size, typee):
        found = False
        min = 1
        if typee == 0:
            while not found:
                x = current_coords[0]+min
                y = current_coords[1]
                if min % size[0] == 0:
                    x += size[0]
                for i in range(0, min+1):
                    if all_coords[x][y] and Imaging.check_space(all_coords, [x, y], size):
                        found = True
                        break
                    if not found:
                        x -= 1
                        y += 1
                min += 1
        elif typee == 1:
            while not found:
                x = current_coords[0]-min
                y = current_coords[1]
                if min % size[0] == 0:
                    x -= size[0]
                for i in range(0, min+1):
                    if all_coords[x][y] and Imaging.check_space(all_coords, [x-size[0], y-size[1]], size):
                        found = True
                        break
                    if not found:
                        x += 1
                        y -= 1
                min += 1
        elif typee == 2:
            while not found:
                x = current_coords[0]
                y = current_coords[1]-min
                if min % size[0] == 0:
                    y -= size[0]
                for i in range(0, min+1):
                    if all_coords[x][y] and Imaging.check_space(all_coords, [x, y-size[0]], [size[1], size[0]]):
                        found = True
                        break
                    if not found:
                        x += 1
                        y += 1
                min += 1
        elif typee == 3:
            while not found:
                x = current_coords[0]
                y = current_coords[1]+min
                if min % size[0] == 0:
                    y += size[0]
                for i in range(0, min+1):
                    if all_coords[x][y] and Imaging.check_space(all_coords, [x-size[1], y], [size[1], size[0]]):
                        found = True
                        break
                    if not found:
                        x -= 1
                        y -= 1
                min += 1
        return x, y

    @staticmethod
    def draw_word(draw, img, fnt, text_options, word, all_coords, x, y, size, typee):
        if typee == 0:
            while not Imaging.check_space(all_coords, [x, y], size):
                x, y = Imaging.get_min_coords(all_coords, [x, y], size, typee)
            draw.text((x, y), word, font=fnt, **text_options)
            Imaging.toggle_coords(all_coords, [x, y], size)
        elif typee == 1:
            while not Imaging.check_space(all_coords, [x-size[0], y-size[1]], size):
                x, y = Imaging.get_min_coords(all_coords, [x, y], size, typee)
            draw.text((x-size[0], y-size[1]), word, font=fnt, **text_options)
            Imaging.toggle_coords(all_coords, [x-size[0], y-size[1]], size)
        else:
            size2 = [size[1], size[0]]
            txt_image = Image.new("RGB", (size[0], size[1]), "red")
            txt_draw = ImageDraw.Draw(txt_image)
            txt_draw.text((0, 0), word, font=fnt, **text_options)
            if typee == 2:
                while not Imaging.check_space(all_coords, [x, y-size[0]], size2):
                    x, y = Imaging.get_min_coords(all_coords, [x, y], size, typee)
                txt_image = txt_image.transpose(Image.ROTATE_90)
                img.paste(txt_image, (x, y-size[0]))
                Imaging.toggle_coords(all_coords, [x, y-size[0]], size2)
            if typee == 3:
                while not Imaging.check_space(all_coords, [x-size[1], y], size2):
                    x, y = Imaging.get_min_coords(all_coords, [x, y], size, typee)
                txt_image = txt_image.transpose(Image.ROTATE_270)
                img.paste(txt_image, (x-size[1], y))
                Imaging.toggle_coords(all_coords, [x-size[1], y], size2)

    @staticmethod
    def cropper(all_coords):
        left, upper, right, lower = 0, 0, 0, 0
        y = 0
        while True:
            x = 0
            while True:
                x += 1
                if x == 1000 or not all_coords[x][y]:
                    break
            if not all_coords[x][y]:
                break
            y += 1
        upper = y
        x = 1000
        while True:
            y = 0
            while True:
                y += 1
                if y == 1000 or not all_coords[x][y]:
                    break
            if not all_coords[x][y]:
                break
            x -= 1
        right = x
        y = 1000
        while True:
            x = 1000
            while True:
                x -= 1
                if x == 0 or not all_coords[x][y]:
                    break
            if not all_coords[x][y]:
                break
            y -= 1
        lower = y
        x = 0
        while True:
            y = 1000
            while True:
                y -= 1
                if y == 0 or not all_coords[x][y]:
                    break
            if not all_coords[x][y]:
                break
            x += 1
        left = x
        return (left, upper, right, lower)

    @staticmethod
    def create_image(list_of_words, filename):

        sorted_list = []
        length = len(list_of_words)
        for i in range(0, length-1):
            max = 0
            for j in range(1, len(list_of_words)):
                if list_of_words[max][1] < list_of_words[j][1]:
                    max = j
            sorted_list.append(list_of_words[max])
            del list_of_words[max]
        sorted_list.append(list_of_words[0])

        all_coordinates = []
        for i in range(0, 1001):
            y_coordinates = []
            for j in range(0, 1001):
                y_coordinates.append(True)
            all_coordinates.append(y_coordinates)

        img = Image.new("RGB", (1000, 1000), "white")
        draw = ImageDraw.Draw(img)
        text_options = {'fill': (sorted_list[0][2][0], sorted_list[0][2][1], sorted_list[0][2][2])}
        fnt = ImageFont.truetype("Later.ttf", (sorted_list[0][1]*6+4))
        draw.text((500, 500), sorted_list[0][0], font=fnt, **text_options)
        size = draw.textsize(sorted_list[0][0], font=fnt)
        Imaging.toggle_coords(all_coordinates, [500, 500], size)
        middle_coords = [[500, 500+size[1]], [500+size[0], 500], [500+size[0], 500+size[1]], [500, 500]]
        del sorted_list[0]
        counter = 0
        for word in sorted_list:
            for typee in range(0, 4):
                if counter >= len(sorted_list):
                    break
                text_options = {'fill': (sorted_list[counter][2][0], sorted_list[counter][2][1],
                                sorted_list[counter][2][2])}
                fnt = ImageFont.truetype("Later.ttf", (sorted_list[counter][1]*6+4))
                size = draw.textsize(sorted_list[counter][0], font=fnt)
                Imaging.draw_word(draw, img, fnt, text_options, sorted_list[counter][0], all_coordinates,
                                  middle_coords[typee][0], middle_coords[typee][1], size, typee)
                counter += 1

        img = img.crop(Imaging.cropper(all_coordinates))
        img.save(filename)
