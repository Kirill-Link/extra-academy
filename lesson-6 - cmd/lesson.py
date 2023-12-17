import os
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнено за {end_time - start_time:.5f} секунд")
        return result
    return wrapper

class CommandPrompt:
    def __init__(self):
        self.current_directory = os.getcwd()

    @execution_time_decorator
    def list_directories(self):
        try:
            directories = os.listdir(self.current_directory)
            for item in directories:
                print(item)
        except Exception as e:
            print(f"Ошибка: {e}")

    @execution_time_decorator
    def change_directory(self, new_directory):
        try:
            os.chdir(new_directory)
            self.current_directory = os.getcwd()
        except Exception as e:
            print(f"Ошибка: {e}")

    @execution_time_decorator
    def create_directory(self, directory_name):
        try:
            os.mkdir(directory_name)
            print(f"Папка {directory_name} создана")
        except Exception as e:
            print(f"Ошибка: {e}")

    @execution_time_decorator
    def delete_directory(self, directory_name):
        try:
            os.rmdir(directory_name)
            print(f"Папка {directory_name} удалена")
        except Exception as e:
            print(f"Ошибка: {e}")

    @execution_time_decorator
    def rename_directory(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Папка {old_name} переименована в {new_name}")
        except Exception as e:
            print(f"Ошибка: {e}")

    @execution_time_decorator
    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    cmd = CommandPrompt()

    while True:
        user_input = input("Введите команду ('help' для списка команд, 'exit' для выхода): ").split()

        if not user_input:
            continue

        command = user_input[0].lower()
        args = user_input[1:]

        if command == 'ls':
            cmd.list_directories()
        elif command == 'cd':
            if args:
                cmd.change_directory(args[0])
            else:
                print("Пожалуйста, укажите имя директории.")
        elif command == 'mkdir':
            if args:
                cmd.create_directory(args[0])
            else:
                print("Пожалуйста, укажите имя директории для создания.")
        elif command == 'rmdir':
            if args:
                cmd.delete_directory(args[0])
            else:
                print("Пожалуйста, укажите имя директории для удаления.")
        elif command == 'rename':
            if len(args) == 2:
                cmd.rename_directory(args[0], args[1])
            else:
                print("Пожалуйста, укажите старое и новое имя директории.")
        elif command == 'read':
            if args:
                cmd.read_file(args[0])
            else:
                print("Пожалуйста, укажите имя файла для чтения.")
        elif command == 'exit':
            print("Удачного пути !!!")
            break
        elif command == 'help':
            print("Доступные команды:\n"
                  "ls - выводит список всех файлов в директории\n"
                  "cd - перемешает по директориям cd <nameFile>\n"
                  "mkdir - создаёт директорию: mkdir <directoryName> \n"
                  "rmdir - удаляет директорию: rmdir <directoryName>\n"
                  "rename - переименовать директорию: rename <directoryName>\n"
                  "read - прочитать файл: read <fileName> \n"
                  "exit - выход с командной строки")
        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")
