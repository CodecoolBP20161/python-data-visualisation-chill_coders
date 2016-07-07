import csv


class Normalisation(object):

    # @staticmethod
    # def open_csv(file_name):
    #     with open(file_name, newline="") as csvfile:
    #         datareader = csv.reader(csvfile, delimiter=",")
    #         list_of_datas = [row for row in datareader]
    #     return list_of_datas

    # def normalize_data_q1(self, file_name):
    #     updated_data = Normalisation.open_csv(file_name)
    #     return updated_data

    def normalize_data_q2(self, file_name): # in runSql(query)
        updated_data = Normalisation.open_csv(file_name)
        for row in updated_data:
            if row[2] == 'GBP':
                row[1] = round(float(row[1]) * 1.17)
            if row[2] == 'USD':
                row[1] = round(float(row[1]) * 0.9)
            if row[2] == 'EUR':
                row[1] = round(float(row[1]))
            del row[2]
        return sorted(updated_data, key=lambda x: x[1], reverse=True)

    def normalize_data_q3(self, file_name):
        updated_data = Normalisation.open_csv(file_name)
        for row in updated_data:
            row[1] = row[1].replace('-', '')
            row[1] = int(row[1][2] + row[1][3])
        return updated_data

    def normalize_data_q4(self, file_name):
        import random

        updated_data = Normalisation.open_csv(file_name)
        counter_1 = 0
        counter_2 = 0
        counter_3 = 0
        counter_4 = 0
        list_of_colors = [row[2] for row in updated_data]
        for row in updated_data:
            if row[1] == '1':
                counter_1 += 1
            if row[1] == '2':
                counter_2 +=1
            if row[1] == '3':
                counter_3 +=1
            if row[1] == '4':
                counter_4 +=1
        updated_data = [
                        ['under order', counter_1, random.choice(list_of_colors)],
                        ['development', counter_2, random.choice(list_of_colors)],
                        ['testing', counter_3, random.choice(list_of_colors)],
                        ['shipped', counter_4, random.choice(list_of_colors)]
        ]
        return updated_data


# q1_data = Normalisation()
q2_data = Normalisation()
q3_data = Normalisation()
q4_data = Normalisation()

# print(q1_data.normalize_data_q1('/home/dorasztanko/Desktop/datas1.csv'))
# ('----------------')
print(q2_data.normalize_data_q2('/home/dorasztanko/Desktop/datas.csv'))
print('------------')
print(q3_data.normalize_data_q3('/home/dorasztanko/Desktop/datas2.csv'))
print('------------')
print(q4_data.normalize_data_q4('/home/dorasztanko/Desktop/datas3.csv'))
