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
        
    
    def login(user, password):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT user,password FROM login")
        usersList = mycursor.fetchall()
        print(usersList)

        for i in usersList:
            if user == i[0] and password == i[1]:
                print(f"Welcome, {user}!")
                break
        else:
            print("Incorrect name or password!")

        mydb.close()
    
class Register(UserActions):
    def __init__(self, user, password):
        super().__init__(user, password)
    
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
    
    def register(self, user, password):
        mydb = connection("user-database")
        mycursor = mydb.cursor()

        mycursor.execute(f"INSERT INTO login (user, password) VALUES ('{user}', '{password}')")
        print(f"User {user} successfully registered!")
        mydb.commit()

        mydb.close()

if __name__ == "__main__":
    # user = Register("na12", "12345678")
    user = Login.login("abc", "12345678")
