import sqlite3

class Scores:
    def __init__(self):
        self.connection = sqlite3.connect("players.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS logins (
                player_id INTEGER PRIMARY KEY,
                username  TEXT UNIQUE
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                results_id INTEGER PRIMARY KEY,
                wins       INTEGER,
                losses     INTEGER,
                ties       INTEGER,
                player_id  TEXT,
                r_start    TEXT,
                p_start    TEXT,
                s_start    TEXT
            )
            """
        )

    def addPlayer(self, name: str) -> None:
        self.cursor.execute("SELECT * FROM results")
        rows = self.cursor.fetchall()
        found = False
        for row in rows:
            if row[4] == name:
                found = True
        if found == False:
            rock = "1,1,1"
            paper = "1,1,1"
            scissors = "1,1,1"
            self.cursor.execute("INSERT OR IGNORE INTO logins (username) VALUES (?)", (name,))
            self.cursor.execute(
                "INSERT OR IGNORE INTO results (wins, losses, ties, player_id, r_start, p_start, s_start) VALUES (0, 0, 0, ?, ?, ?, ?)",
                (name, rock, paper, scissors,),
            )
            self.connection.commit()
    def update(self, rock, paper, scissors, name):
        self.cursor.execute("UPDATE results SET r_start = ? WHERE player_id = ?", (rock, name,))
        self.cursor.execute("UPDATE results SET p_start = ? WHERE player_id = ?", (paper, name,))
        self.cursor.execute("UPDATE results SET s_start = ? WHERE player_id = ?", (scissors, name,))
        self.connection.commit()
    def getArray(self, name):
        array = []
        self.cursor.execute("SELECT * FROM results")
        rows = self.cursor.fetchall()
        for row in rows:
            if row[4] == name:
                array.append(row[5])
                array.append(row[6])
                array.append(row[7])
        return array
    def addScores(self, name: str, delta: int) -> None:
        if delta > 0:
            self.cursor.execute(
                "UPDATE results SET wins = wins + 1 WHERE player_id = ?", (name,)
            )
            self.connection.commit()
        elif delta < 0:
            self.cursor.execute(
                "UPDATE results SET losses = losses + 1 WHERE player_id = ?", (name,)
            )
            self.connection.commit()
        else:
            self.cursor.execute(
                "UPDATE results SET ties = ties + 1 WHERE player_id = ?", (name,)
            )
            self.connection.commit()