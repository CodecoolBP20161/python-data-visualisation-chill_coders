from operator import Operator
import datetime


class Normalisation(object):
    """ Normalizes incoming data if it is needed (per queries). """

    @staticmethod
    def normalize_data_q2(updated_data):
        for row in updated_data:
            if row[2] == 'GBP':
                row[1] = round(float(row[1]) * 1.17)
            if row[2] == 'USD':
                row[1] = round(float(row[1]) * 0.9)
            if row[2] == 'EUR':
                row[1] = round(float(row[1]))
            del row[2]
        return sorted(updated_data, key=lambda x: x[1], reverse=True)

    @staticmethod
    def normalize_data_q3(updated_data):
        for row in updated_data:
            row[1] = row[1].year - 2000
        return updated_data

    @staticmethod
    def normalize_data_q5(updated_data):
        counter_1 = 0
        counter_2 = 0
        counter_3 = 0
        counter_4 = 0
        list_of_colors = [row[2] for row in updated_data]
        for row in updated_data:
            if row[1] == 1:
                counter_1 += 1
            if row[1] == 2:
                counter_2 += 1
            if row[1] == 3:
                counter_3 += 1
            if row[1] == 4:
                counter_4 += 1
        updated_data = [
                        ['under order', counter_1, list_of_colors[0]],
                        ['development', counter_2, list_of_colors[1]],
                        ['testing', counter_3, list_of_colors[2]],
                        ['shipped', counter_4, list_of_colors[3]]
        ]
        return updated_data
