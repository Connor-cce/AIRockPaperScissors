import sqlite3

# define connection and cursor

connection = sqlite3.connect('players.db')

cursor = connection.cursor()

# create player table

command1 = """CREATE TABLE IF NOT EXISTS
player(player_id INTEGER PRIMARY KEY, names TEXT)"""

cursor.execute(command1)

# create player results

command2 = """CREATE TABLE IF NOT EXISTS
results(results_id INTEGER PRIMARY KEY, wins INTEGER, loss INTEGER, player_id INTEGER)"""

cursor.execute(command2)

# add to player table

cursor.execute("INSERT INTO player VALUES (1, 'Connor')")
cursor.execute("INSERT INTO player VALUES (2, 'Yuktha')")
cursor.execute("INSERT INTO player VALUES (3, 'Josue')")

# add to results
cursor.execute("INSERT INTO results VALUES (1, 10, 12)")
cursor.execute("INSERT INTO results VALUES (2, 15, 9)")
cursor.execute("INSERT INTO results VALUES (3, 20, 20)")

# get results

cursor.execute("SELECT * FROM results")

results = cursor.fetchall()
print(results)