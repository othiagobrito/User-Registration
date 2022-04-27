from connection import connection

def create_db(db_name):
    mydb = connection(db_name)
    print(f"Database named '{db_name}' was successfully created!")

    mydb.close()

def create_table(db_name, table_name):
    mydb = connection(db_name)
    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, user TEXT, password TEXT)")
    print(f"Table named '{table_name}' was successfully created!")

    mydb.close()

if __name__ == "__main__":
    db_name = "user-database"
    table_name = "login"

    create_db(db_name)
    create_table(db_name, table_name)
