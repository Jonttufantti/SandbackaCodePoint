import sqlite3
from tabulate import tabulate

# Establish connection
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()

# SQL queries
SQL_TILAT = "SELECT * FROM tilat"
SQL_VARAAJAT = "SELECT * FROM varaajat"
SQL_VARAUKSET = """
    SELECT 
        varaukset.id,
        tilat.tilan_nimi AS tila,
        varaajat.nimi AS varaaja,
        varaukset.varauspaiva
    FROM 
        varaukset
    INNER JOIN 
        tilat ON varaukset.tila = tilat.id
    INNER JOIN 
        varaajat ON varaukset.varaaja = varaajat.id
"""

# Execute queries and fetch results
cursor.execute(SQL_TILAT)
tilat_rows = cursor.fetchall()

cursor.execute(SQL_VARAAJAT)
varaajat_rows = cursor.fetchall()

cursor.execute(SQL_VARAUKSET)
varaukset_rows = cursor.fetchall()

# Display tables side by side
print("Tilat Table:")
print(tabulate(tilat_rows, headers=["ID", "Tilan Nimi"], tablefmt="grid"))

print("\nVaraajat Table:")
print(tabulate(varaajat_rows, headers=["ID", "Nimi"], tablefmt="grid"))

print("\nVaraukset Table:")
print(tabulate(varaukset_rows, headers=["ID", "Tila", "Varaaja", "Varauspäivä"], tablefmt="grid"))

# Close connection
conn.close()
