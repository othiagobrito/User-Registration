from connection import connection

def showTable():
    mydb = connection("user-database")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM login")
    usersList = mycursor.fetchall()

    for id, user, password in usersList:
        txt = f"ID: {id}\tUSER: {user}\tPASSWORD: {password}"
        print(txt)

if __name__ == "__main__":
    showTable()
