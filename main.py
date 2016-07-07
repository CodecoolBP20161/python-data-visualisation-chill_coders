# Query 1: clients according to intensity (number of projects)
"""SELECT company_name, replace(main_color, '#', '') as short_hex_color FROM project WHERE main_color IS NOT NULL;"""

# average color nem jó! ide külön metódust kell írni, ami azt a tuple-listát továbbítja,
# amivel a továbbiakban lehet dolgozni! RETURN!

# Query 2: projects according to value in the same currency
"""SELECT name, budget_value, budget_currency, REPLACE(main_color, '#', '') AS main_color
FROM project WHERE name IS NOT NULL AND main_color IS NOT NULL;"""

# átváltás egységes currency-ba! RETURN new_list of tuples

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

# OPTIMALIZÁLÁS!!!! STATICMETHODOK


# MENU ----------------------------------------------------------------------------------------------------------------

def choose_query(query):
    pass

print("""--- ChillCoders\' PicGenerator is ready to be used! ---

Choose a number from 1 to 5 create a WordCloud!

*** HELP ***
1: clients (company_name) according to intensity (number of projects)
2: projects according to budget_value
3: Easel's projects (highest number of projects) according to duedate
4: Company headquarters according to budget_value (currency: GBP)
5: Categories of status according to number of projects
""")

number = input('Choosen number is: ')

while True:
    try:
        if number == '1':
            # függvénymeghívás
            # break()
            # KISZERVEZNI!
        if number == '2':

        if number == '3':

        if number == '4':

        if number == '5':
    except ValueError:
        print('Invalid input! Try again!')
