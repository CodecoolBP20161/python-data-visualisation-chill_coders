# MENU

# Query 1
"""SELECT company_name, replace(main_color, '#', '') as short_hex_color FROM project WHERE main_color IS NOT NULL;"""

# Query 2
"""SELECT name, budget_value, budget_currency, REPLACE(main_color, '#', '') AS main_color
FROM project WHERE name IS NOT NULL AND main_color IS NOT NULL;"""

# Query 3
"""SELECT name, duedate, replace(main_color, '#', '') AS main_color FROM project
WHERE company_name = 'Eadel' AND name IS NOT NULL
ORDER BY duedate DESC;"""

# Query 4
"""SELECT company_hq, CAST(budget_value AS FLOAT), replace(main_color, '#', '') AS main_color FROM project
WHERE budget_currency = 'GBP' AND company_hq IS NOT NULL AND main_color IS NOT NULL
ORDER BY budget_value DESC;"""

# Query 5
