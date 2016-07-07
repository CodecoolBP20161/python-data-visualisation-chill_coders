from dbconnection import DbConnection
import math

class Operator():

    newlist = []
    newlist2 = []

    @staticmethod
    def operator_main(order = ""):
        wordslist = []
        for words in DbConnection.runSql("""SELECT company_name, replace(main_color, '#', '') as short_hex_color FROM project WHERE main_color IS NOT NULL;"""):
            wordslist.extend([(words[0], words[1])])
        if order == "":
            z = Operator.colors(wordslist)
        if order == "q1":
            a = Operator.q1_colors(wordslist)
            b = Operator.q1_coloravg1(a)
            c = Operator.q1_coloravg2(b)


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
                Operator.newlist.append(word)
            for i in Operator.newlist:
                if i not in Operator.newlist2:
                    Operator.newlist2.append(i)
            x += 1
            b -= 1
            if b == 0:
                return Operator.newlist2

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

Operator.operator_main("")

