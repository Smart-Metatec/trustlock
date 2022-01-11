import sqlite3
import os

path = os.getenv("APPDATA") + "\\WorkMate"

class Model:
    def __init__(self):
        self.db = sqlite3.connect(f"./database/workmate.db")
        self.cur = self.db.cursor()

        self.create_tables()

    def create_tables(self):
        apps_table = """
            CREATE TABLE IF NOT EXISTS apps(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                path TEXT NOT NULL,
                sequence INTEGER NOT NULL,
                username TEXT,
                email TEXT,
                password TEXT NOT NULL
            )
        """

        notes_table = """
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                body TEXT
            )
        """

        todos_table = """
            CREATE TABLE IF NOT EXISTS todos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                complete INTEGER DEFAULT 0 NOT NULL,
                deadline TEXT
            )
        """

        settings_table = """
            CREATE TABLE IF NOT EXISTS settings(
                id TEXT DEFAULT 'settings' PRIMARY KEY,
                nightmode INTEGER DEFAULT 0,
                font TEXT DEFAULT 'Arial',
                color TEXT DEFAULT '#000000',
                vault_on INTEGER DEFAULT 1 NOT NULL,
                timer INTEGER DEFAULT 5 NOT NULL,
                calendar INTEGER DEFAULT 0 NOT NULL
            )
        """

        users_table = """
            CREATE TABLE IF NOT EXISTS user(
                id TEXT DEFAULT 'user' PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        """

        vault_table = """
            CREATE TABLE IF NOT EXISTS vault(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """
        self.cur.execute(apps_table)
        self.cur.execute(notes_table)
        self.cur.execute(todos_table)
        self.cur.execute(settings_table)
        self.cur.execute(users_table)
        self.cur.execute(vault_table)

    def save(self, table, data): 
        keys = f'{", ".join(data.keys())}'
        values = ", ".join(list(map(lambda v: "?", data.keys())))

        query = f"INSERT INTO {table}({keys}) VALUES ({values})"

        self.cur.executemany(query, [tuple(data.values())])
        self.db.commit()
        self.db.close()
        
        

    def read(self, table):

        query = f"SELECT * FROM {table}"
        
        self.cur.execute(query)
        data = self.cur.fetchall()
        self.db.close()

        return data

    def delete(self, table, id):
        query = f"DELETE FROM {table} WHERE id = (?)"
        self.cur.execute(query, (id,))
        self.db.commit()
        self.db.close()

    def update(self, table, data, id):
        fields = data.keys()
        values = list(data.values())
        values.append(id)
        data_string = ", ".join(list(map(lambda a: f"{a} = ?", fields)))
        

 
        query = f"UPDATE {table} SET {data_string} WHERE id = ?"

        self.cur.execute(query, values)
        self.db.commit()
        self.db.close()
    
    def clearTable(self, table):
        query = f"""
            DROP TABLE IF EXISTS {table}
        """
        self.cur.execute(query)
        self.db.commit()
        self.db.close()
    
    def reset(self):
        query = """
            UPDATE settings SET nightmode = 0, font = 'Arial', color = '#000000' WHERE id = 'settings'
        """

        self.cur.execute(query)
        self.db.commit()
        self.db.close()
    
    def start(self):
        settings = Model().read("settings")
        if len(settings) == 0:
            data = {
                'nightmode': 0,
                'font': "Arial",
                'color': "#000000"
            }
            self.save('settings', data)

# Model().clearTable("user")
# Model().clearTable("settings")









    
    
        