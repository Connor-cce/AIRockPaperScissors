import sqlite3

# cursor.execute("SELECT * FROM results")

# results = cursor.fetchall()
# print(results)
# cursor.execute("UPDATE results SET wins = 10 WHERE results_id = 2")
# cursor.execute("DELETE FROM purchases WHERE purchase_id = 54")
connection = sqlite3.connect('store_players.db')
cursor = connection.cursor()

class Scores():

    def __init__(self):
        command1 = """CREATE TABLE IF NOT EXISTS
        logins(player_id INTEGER PRIMARY KEY, username TEXT)"""

        cursor.execute(command1)

        command2 = """CREATE TABLE IF NOT EXISTS
        results(results_id INTEGER PRIMARY KEY, wins INTEGER, losses INTEGER, ties INTEGER, player_id TEXT)"""

        cursor.execute(command2)

    def addPlayer(self, name):
        addLogin = "INSERT INTO logins (name) values (?)"
        addResults = "INSERT INTO results (wins, losses, ties, player_id) values (?, ?, ?, ?)"
        cursor.execute(addLogin, (name))
        cursor.execute(addResults, (0, 0, 0, name))
    # def findPlayer(self, name):
    #     cursor.execute("SELECT * FROM logins")
    #     output = cursor.fetchall
    #     for row in output:
    #         if row == name:
    #             return True
    #     return False
    def addScores(self, name, score):
        if (score > 0):
            cursor.execute(f"UPDATE results SET wins = wins + 1 WHERE player_id = {name}")
        elif (score < 0):
            cursor.execute(f"UPDATE results SET losses = losses + 1 WHERE player_id = {name}")
        else:
            cursor.execute(f"UPDATE results SET ties = ties + 1 WHERE player_id = {name}")
