class User:
    def __init__(self, id, name, login, password, authorize):
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.authorize = authorize

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getLogin(self):
        return self.login

    def getPassword(self):
        return self.password

    def getAuthorize(self):
        return self.authorize

    def setAuthorize(self, state):
        self.authorize = state

class IUserManager(User):
    def logIn(self, bd):
        bdUsers = bd.getBD()
        for i in bdUsers:
            if i.getLogin == self.getLogin():
                print("Пользователь с таким логином уже сущестует")
                return False
        bd.addOnBD(self)
        print(f"Пользователь - {self.getName()} зарегистрирван!")

    def signIn(self):
        lk = True
        while lk:
            print("Это личный кабинет!")
            print("1 - Выйти")
            if int(input()) == 1:
                lk = self.signOut()
    def signOut(self):
        print("Вы вышли из личного кабинета!")
        return False



class IUserRepository:
    def __init__(self):
        self.bd = []

    def addOnBD(self, user):
        self.bd.append(user)

    def getBD(self):
        return self.bd

    def delOnBD(self, id):
        del self.bd[id]

    def searchUser(self, login, password):
        for i in self.bd:
            if i.getLogin() == login:
                if i.getPassword() == password:
                    print("Вы вошли в личный кабинет!")
                    return i
                else:
                    print("Неправильный пароль")
                    return None
        print("Такого пользователя не существует!")
        return None

    def printAutorizeUsers(self):
        for i in self.bd:
            if i.getAuthorize():
                print((i.getId()+1), "-", i.getName())

    def printAllUsers(self):
        for i in self.bd:
            print("------------------")
            print("Id - ", i.getId())
            print("Name - ", i.getName())
            print("Login - ", i.getLogin())
            print("Password - ", i.getPassword())
            print("Authorize - ", i.getAuthorize())


if __name__ == '__main__':
    bd = IUserRepository()
    testUser = IUserManager(0, 'Danil', '123', '123', True)
    bd.addOnBD(testUser)

    run = True
    while run:
        print("1 - Зарегистрироваться")
        print("2 - Войти")
        print("3 - Выйти")
        step = int(input())
        if step == 1:
            print("Введите ваше имя!\n")
            name = str(input())
            print("Логин: ")
            login = str(input())
            print("Пароль: ")
            password = str(input())
            print("Сохранить данные о входе? (Да/Нет)")
            authorize = str(input())
            if (authorize == 'Да'):
                user = IUserManager(len(bd.getBD()), name, login, password, True) # задем id так чтобы они не повторялись
                user.logIn(bd)
            elif (authorize == 'Нет'):
                user = IUserManager(len(bd.getBD()), name, login, password, False)
                user.logIn(bd)
            else:
               print("Неправильный ввод двнных")

        if step == 2:
            print("Вы авторизованы? (Да/Нет)")
            authorize = str(input())
            if (authorize == 'Да'):
                bd.printAutorizeUsers()
                print("Выберите номер аккаунта под которым вы заходили")
                number = int(input())
                bd.getBD()[number - 1].signIn()
            elif (authorize == 'Нет'):
                print("Введите")
                print("Логин: ")
                login = str(input())
                print("Пароль: ")
                password = str(input())
                user = bd.searchUser(login, password)
                if user is not None:
                    user.signIn()
                else:
                    print("Пользователь не найден!")
            else:
                print("Неправильный ввод двнных!")
        if step == 3:
            run = False
            print("Пока")