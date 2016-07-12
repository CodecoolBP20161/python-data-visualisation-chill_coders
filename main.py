from engine import Engine
from normalisation import Normalisation
from imaging import Imaging

# Query 1: clients according to intensity (number of projects)
"""SELECT company_name, replace(main_color, '#', '') as short_hex_color FROM project WHERE main_color IS NOT NULL;"""

# Query 2: projects according to value in the same currency
"""SELECT name, budget_value, budget_currency, REPLACE(main_color, '#', '') AS main_color
FROM project WHERE name IS NOT NULL AND main_color IS NOT NULL;"""

# Query 3: Easel's projects (highest number of projects) according to duedate
"""SELECT name, duedate, replace(main_color, '#', '') AS main_color FROM project
WHERE company_name = 'Eadel' AND name IS NOT NULL
ORDER BY duedate DESC;"""

# Query 4: Company headquarters according to budget_value (currency: GBP)
"""SELECT company_hq, budget_value, replace(main_color, '#', '') AS main_color FROM project
WHERE budget_currency = 'GBP' AND company_hq IS NOT NULL AND main_color IS NOT NULL
ORDER BY CAST(budget_value AS FLOAT) DESC;"""

# Query 5: Categories of status according to number of projects
"""SELECT name, status, REPLACE(main_color, '#', '') AS main_color FROM project
WHERE name IS NOT NULL AND main_color IS NOT NULL
ORDER BY status DESC;"""


# MENU ----------------------------------------------------------------------------------------------------------------

print("""--- ChillCoders\' PicGenerator is ready to be used! ---

Choose a number from 1 to 5 create a WordCloud!

*** HELP ***
1: clients (company_name) according to intensity (number of projects)
2: projects according to budget_value
3: Easel's projects (highest number of projects) according to duedate
4: Company headquarters according to budget_value (currency: GBP)
5: Categories of status according to number of projects
""")

while True:
    number = input('Choosen number is: ')

    if number == '1':
        q1 = """SELECT company_name, replace(main_color, '#', '') as short_hex_color
                FROM project
                WHERE main_color IS NOT NULL;"""
        order = "q1"
        Imaging.create_image(Engine.engine_main(q1, order), 'pic1.png')
        exit()

    if number == '2':
        q2 = """SELECT name, budget_value, budget_currency, REPLACE(main_color, '#', '') AS main_color
                FROM project
                WHERE name IS NOT NULL
                AND main_color IS NOT NULL;"""
        order = "q4"
        normalised_incoming_datalist = Normalisation.normalize_data_q2(Engine.engine_main(q2, order))
        Imaging.create_image(Engine.getsize(normalised_incoming_datalist)[:20], 'pic2.png')
        exit()

    if number == '3':
        q3 = """SELECT name, duedate, replace(main_color, '#', '') AS main_color
                FROM project
                WHERE company_name = 'Eadel'
                AND name IS NOT NULL ORDER BY duedate DESC;"""
        order = ""
        normalised_incoming_datalist = Normalisation.normalize_data_q3(Engine.engine_main(q3, order))
        Imaging.create_image(Engine.getsize(normalised_incoming_datalist), 'pic3.png')
        exit()

    if number == '4':
        q4 = """SELECT company_hq, CAST(budget_value AS float), replace(main_color, '#', '') AS main_color
                FROM project
                WHERE budget_currency = 'GBP'
                AND company_hq IS NOT NULL
                AND main_color IS NOT NULL ORDER BY CAST(budget_value AS FLOAT) DESC;"""
        order = ""
        normalised_incoming_datalist = Engine.engine_main(q4, order)
        Imaging.create_image(Engine.getsize(normalised_incoming_datalist), 'pic4.png')
        exit()

    if number == '5':
        q5 = """SELECT name, status, REPLACE(main_color, '#', '') AS main_color
                FROM project
                WHERE name IS NOT NULL
                AND main_color IS NOT NULL ORDER BY status DESC;"""
        order = ""
        normalised_incoming_datalist = Normalisation.normalize_data_q5(Engine.engine_main(q5, order))
        Imaging.create_image(Engine.getsize(normalised_incoming_datalist), 'pic5.png')
        exit()

    else:
        print('Invalid input!')
        exit()
