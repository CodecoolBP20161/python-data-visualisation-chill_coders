import psycopg2

class DbConnection:

    @staticmethod
    def open_file(file_name):
        with open(file_name, "r") as f:
            data_line = f.readlines()
            return data_line[0].replace('\n', '')

    @staticmethod
    def runSql(query):
        try:
            connect_str = DbConnection.open_file('.git/db_config.txt')
            conn = psycopg2.connect(connect_str)
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)