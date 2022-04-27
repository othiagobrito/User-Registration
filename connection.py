def connection(db_name):
    import sqlite3

    mydb = sqlite3.connect(f"{db_name}.db")
    return mydb

if __name__ == "__main__":
    db_name = ""

    connection(db_name)
