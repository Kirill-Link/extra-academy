user_list = []

def print_menu():
    print("1. Добавить пользователя")
    print("2. Редактировать пользователя")
    print("3. Удалить пользователя")
    print("4. Посмотреть список пользователей")
    print("5. Войти")
    print("6. Выйти")


def add_user():
    user = {}
    user["Name"] = input("Введите имя: ")
    user["Surname"] = input("Введите фамилию: ")
    while True:
        try:
            user["Age"] = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Ошибка! Возраст должен быть числом.")
    user["Address"] = input("Введите адрес: ")
    user["Username"] = input("Введите имя пользователя: ")

    while True:
        password = input("Введите пароль (минимум 8 символов): ")
        if len(password) >= 8:
            user["Password"] = password
            break
        else:
            print("Ошибка! Пароль должен содержать минимум 8 символов.")

    while True:
        email = input("Введите уникальную почту: ")
        if not any(u["Username"] == email for u in user_list):
            user["Email"] = email
            break
        else:
            print("Ошибка! Почта должна быть уникальной.")

    user_list.append(user)
    print("Пользователь добавлен успешно.")


def edit_user():
    username = input("Введите имя пользователя для редактирования: ")
    for user in user_list:
        if user["Username"] == username:
            user["Name"] = input(f"Введите новое имя для {username}: ")
            user["Surname"] = input(f"Введите новую фамилию для {username}: ")
            user["Age"] = int(input(f"Введите новый возраст для {username}: "))
            user["Address"] = input(f"Введите новый адрес для {username}: ")
            user["Password"] = input(f"Введите новый пароль для {username} (минимум 8 символов): ")
            while len(user["Password"]) < 8:
                print("Ошибка! Пароль должен содержать минимум 8 символов.")
                user["Password"] = input(f"Введите новый пароль для {username} (минимум 8 символов): ")
            print("Пользователь успешно отредактирован.")
            return
    print(f"Пользователь с именем пользователя {username} не найден.")


def delete_user():
    username = input("Введите имя пользователя для удаления: ")
    for user in user_list:
        if user["Username"] == username:
            user_list.remove(user)
            print(f"Пользователь {username} успешно удален.")
            return
    print(f"Пользователь с именем пользователя {username} не найден.")


def view_users():
    print("Список пользователей:")
    for user in user_list:
        print(
            f"Имя: {user['Name']}, Фамилия: {user['Surname']}, Возраст: {user['Age']}, Адрес: {user['Address']}, Имя пользователя: {user['Username']}, Почта: {user['Email']}")
    print()


def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    for user in user_list:
        if user["Username"] == username and user["Password"] == password:
            print("Вход выполнен успешно.")
            return
    print("Неверное имя пользователя или пароль.")


while True:
    print_menu()
    choice = input("Выберите действие (1-6): ")

    if choice == "1":
        add_user()
    elif choice == "2":
        edit_user()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        view_users()
    elif choice == "5":
        login()
    elif choice == "6":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")
