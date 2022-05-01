from collections import UserList
from connection import connection

class UserActions:
    def __init__(self, user, password):
        self.user = user
        self.password = password
    

class Login(UserActions):
    def __init__(self, user, password):
        super().__init__(user, password)

        self.user = user
        self.password = password

        self.login(user, password)
        
    
    def login(self, user, password):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT user,password FROM login WHERE user='{user}' and password='{password}'")
        usersList = mycursor.fetchall()

        if usersList:
            print(f"Welcome, {usersList[0][0]}")
        else:
            print("Incorrect name or password!")

        mydb.close()
    
class Register(UserActions):
    def __init__(self, user, password):
        super().__init__(user, password)

        if self.check_user(user):
            print(f"{self.user} already exists!")
        else:
            if len(user) >= 3:
                self.user = user
            else:
                raise ValueError("Invalid username. Username must have 3 or more characters!")
                
            if len(password) >= 8:
                self.password = password
            else:
                raise ValueError("Invalid password. Password must have 8 to 15 characters!")

            if self.user and self.password:
                self.register(user, password)
    
    def check_user(self, user):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT user,password FROM login WHERE user='{user}'")
        usersList = mycursor.fetchall()

        return usersList

    def register(self, user, password):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"INSERT INTO login (user, password) VALUES ('{user}', '{password}')")
        print(f"User {user} successfully registered!")
        mydb.commit()

        mydb.close()

if __name__ == "__main__":
    # user = Register("na12", "12345678")
    user = Login("abc", "12345678")
