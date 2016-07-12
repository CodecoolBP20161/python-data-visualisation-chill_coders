from dbconnection import DbConnection


class Engine():
    """ Optimises parameters. """

    newlist = []
    newlist2 = []

    @staticmethod
    def engine_main(query, order=""):
        wordslist = [word for word in DbConnection.runSql(query)]
        if order == "":
            return Engine.colors(wordslist)
        if order == "q1":
            a = Engine.q1_colors(wordslist)
            b = Engine.q1_coloravg1(a)
            c = Engine.q1_coloravg2(b)
            return Engine.getsize(c)
        if order == "q4":
            return Engine.q4_colors(wordslist)

    @staticmethod
    def getsize(data_list):
        from math import ceil

        number_of_datas = len(data_list)
        data_list = sorted(data_list, key=lambda x: x[1], reverse=True)

        a_max = max([data[1] for data in data_list])
        a_min = min([data[1] for data in data_list])

        for element in data_list:
            element[1] = ceil(float(element[1]) * (1 / a_max) * 10)

        for element in data_list:
            if element[1] == 0:
                element[1] += 1

        return data_list

    @classmethod
    def colors(cls, wordlist):
        alist = []
        for element in wordlist:
            a = ''.join([x * 2 for x in element[-1][:]])
            b = tuple(int(a[i:i + 2], 16) for i in (0, 2, 4))
            newelement = [element[0], element[1], b]
            alist.append(newelement)
        return alist

    @classmethod
    def q1_colors(cls, wordlist):
        alist = []
        for element in wordlist:
            a = ''.join([x * 2 for x in element[1][:]])
            b = tuple(int(a[i:i + 2], 16) for i in (0, 2, 4))
            newelement = [element[0], b]
            alist.append(newelement)
        return alist

    @classmethod
    def q4_colors(cls, wordlist):
        alist = []
        for element in wordlist:
            a = ''.join([x * 2 for x in element[-1][:]])
            b = tuple(int(a[i:i + 2], 16) for i in (0, 2, 4))
            newelement = [element[0], element[1], element[2], b]
            alist.append(newelement)
        return alist

    @classmethod
    def q1_coloravg1(cls, wordlist):
        x = 0
        b = len(wordlist)
        a = len(wordlist)
        while x != b:
            z = 0
            while z != len(wordlist):
                word = []
                sizecount = 0
                for element in wordlist:
                    if wordlist[x][0] == element[0]:
                        word.append(element)
                        sizecount += 1
                    z += 1
                word.append(sizecount)
                Engine.newlist.append(word)
            for i in Engine.newlist:
                if i not in Engine.newlist2:
                    Engine.newlist2.append(i)
            x += 1
            b -= 1
            if b == 0:
                return Engine.newlist2

    @classmethod
    def q1_coloravg2(cls, wordlist):
        size = []
        finallist = []
        rgblist = []
        for element in wordlist:
            newlist = []
            newlist.append(element[0][0])
            for elem in element[:-1]:
                newlist.append(elem[1])
            rgblist.append(newlist)
            size.append(element[-1])
        for element in rgblist:
            rgbavglist = []
            r = []
            g = []
            b = []
            for elem in element[1:]:
                r.append(elem[0])
                g.append(elem[1])
                b.append(elem[2])
            r = sum(r) // len(r)
            g = sum(g) // len(g)
            b = sum(b) // len(b)
            rgbavglist.extend([element[0], (r, g, b)])
            finallist.append(rgbavglist)
        x = 0
        for element in finallist:
            element.insert(1, size[x])
            x += 1
        return finallist
