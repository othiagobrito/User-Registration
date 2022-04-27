from connection import connection

class User:
    def __init__(self, user, password):
        if len(user) >= 3:
            self.user = user
        else:
            raise ValueError("Invalid username. Username must have 3 or more characters!")
        
        if len(password) >= 8:
            self.password = password
        else:
            raise ValueError("Invalid password. Password must have 8 to 15 characters!")

    def addUser(self):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"INSERT INTO login (user, password) VALUES ('{self.user}', '{self.password}')")
        print(f"User {self.user} successfully registered!")
        mydb.commit()

        mydb.close()
    
    def loginUser(self, user, password):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT user,password FROM login")
        usersList = mycursor.fetchall()

        for userList, passwordList in usersList:
            if user == userList and password in passwordList:
                print(f"Welcome, {user}!")
            else:
                print("Incorrect name or password!")

        mydb.close()

    
if __name__ == "__main__":
    user = User("abc", "12345678")
    # user.addUser()

    user.loginUser("teste", "12345678")
