from dbconnection import DbConnection
import math

class Operator():

    @staticmethod
    def operator_main():
        wordslist = []
        for words in DbConnection.runSql("""SELECT company_hq, replace(main_color, '#', '') AS main_color FROM project WHERE budget_currency = 'GBP' AND company_hq IS NOT NULL AND main_color IS NOT NULL ORDER BY CAST(budget_value AS FLOAT) DESC;"""):
            wordslist.extend([(words[0], words[1])])
        a = Operator.colors(wordslist)
        b = Operator.coloravg(a)
        newlist = []
        for element in a:
            element[1] = b
            newlist.append(element)
        return Operator.give_size(newlist)




    @classmethod
    def colors(cls, wordlist):
        alist = []
        for element in wordlist:
            a = ''.join([x * 2 for x in element[1][:]])
            b = tuple(int(a[i:i + 2], 16) for i in (0, 2, 4))
            newelement = [element[0], b]
            alist.append(newelement)
        return alist

    @classmethod
    def coloravg(cls, wordlist):
        r = []
        g = []
        b = []
        for element in wordlist:
            r.append(element[1][0])
            g.append(element[1][1])
            b.append(element[1][2])
        rfin = sum(r) // len(r)
        gfin = sum(g) // len(g)
        bfin = sum(b) // len(b)
        return (rfin, gfin, bfin)

    @classmethod
    def give_size(cls, wordlist):
        a = len(wordlist) / 100
        for element in wordlist[0:math.ceil(a*1)]:
            element.append(10)
        for element in wordlist[math.ceil(a*2):math.ceil(a*6)]:
            element.append(9)
        for element in wordlist[math.ceil(a*6):math.ceil(a*10)]:
            element.append(8)
        for element in wordlist[math.ceil(a*10):math.ceil(a*20)]:
            element.append(7)
        for element in wordlist[math.ceil(a*20):math.ceil(a*60)]:
            element.append(6)
        for element in wordlist[math.ceil(a*60):math.ceil(a*70)]:
            element.append(5)
        for element in wordlist[math.ceil(a*70):math.ceil(a*70)]:
            element.append(4)
        for element in wordlist[math.ceil(a*70):math.ceil(a*80)]:
            element.append(3)
        for element in wordlist[math.ceil(a*80):math.ceil(a*90)]:
            element.append(2)
        for element in wordlist[math.ceil(a*90):math.ceil(a*100)]:
            element.append(1)
        return wordlist



Operator.operator_main()

