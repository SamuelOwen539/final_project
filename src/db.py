import sqlite3


class DB():
    def __init__(self):
        self.connection = sqlite3.connect("data/db_sql.db")

    def make_table(self):

        drop_teams = '''
        DROP TABLE IF EXISTS "Locations";
        '''

        create_table = '''
            CREATE TABLE IF NOT EXISTS "Locations" (
                "Id"        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "City"  TEXT NOT NULL,
                "Restaurant" TEXT NOT NULL,
                "Rating"  INTEGER NOT NULL,
                "Price"    TEXT NOT NULL
            );
    '''
        cursor = self.connection.cursor()
        cursor.execute(create_table)
        self.connection.commit()

    def entry(self, data):
        self.make_table()
        cursor = self.connection.cursor()
        cursor.execute(

            f'''
            INSERT INTO Locations(City, Restaurant, Rating, Price)
            values("{data[0]}", "{data[1]}", "{data[2]}", "{data[3]}");
            '''
        )
        self.connection.commit()

    def query(self, city):
        cursor = self.connection.cursor()
        cursor.execute(

            f'''
            SELECT City, Restaurant, Rating, Price FROM Locations WHERE City = "{city}"
            '''
        )
        return cursor.fetchall()






if __name__ == "__main__":

    db = DB()
    db.query('Locations')
    #db.entry('Locations', ['test1', 'test2', 3, 'test4'])

    db.connection.close()
    

