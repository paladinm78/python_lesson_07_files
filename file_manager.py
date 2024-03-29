import os
import platform
import shutil

from input_functions import confirmation


def make_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        return f"Папка '{folder_name}' успешно создана."
    except OSError as error:
        return f"Ошибка при создании папки: {error}"


def remove_file_or_folder(object_name):
    if not os.path.exists(object_name):
        return "Файл или папка не найдены."

    if os.path.isfile(object_name):
        # Удаляем файл
        os.remove(object_name)
        return f"Файл '{object_name}' был удален."
    elif os.path.isdir(object_name):
        # Удаляем папку
        shutil.rmtree(object_name)
        return f"Папка '{object_name}' была удалена."


def copy_file_or_folder(source, destination):

    if not os.path.exists(source):
        return f'Не найдено файла или папки с названием {source}'

    if os.path.isfile(source):
        try:
            shutil.copy(source, destination)
            return f"Файл '{source}' скопирован в '{destination}'"
        except IOError as error:
            return f"Не удалось скопировать файл. Ошибка: {error}"
    elif os.path.isdir(source):
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            return f"Папка '{source}' скопирована в '{destination}'"
        except shutil.Error as error:
            return f"Не удалось скопировать папку. {error}"
    else:
        return f'{source} не является папкой или файлом'


def list_dir(show_folders=True, show_files=True):
    contents = os.listdir()
    objets_list = []
    for item in contents:
        if show_folders and os.path.isdir(item):
            objets_list.append(item)
        if show_files and os.path.isfile(item):
            objets_list.append(item)
    return objets_list


def show_platform_info():
    info_list = []

    platform_info = platform.platform()
    info_list.append(f"Платформа: {platform_info}")

    architecture = platform.architecture()
    info_list.append(f"Архитектура: {architecture}")

    processor_info = platform.processor()
    info_list.append(f"Процессор: {processor_info}")

    return info_list


def change_work_directory(new_directory):
    try:
        os.chdir(new_directory)
        return f"Текущая рабочая директория изменена на: {os.getcwd()}"
    except Exception as e:
        return f"Ошибка при смене директории: {e}"



def show_file_manager_menu():
    print()
    print('Консольный файловый менеджер')
    print()
    print('Меню:')
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. посмотреть содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('8. просмотр информации об операционной системе')
    print('9. смена рабочей директории')
    print('10. выход')
    print()


def run_file_manager():

    while True:
        show_file_manager_menu()
        choice = input('Выберите пункт меню: ')
        print()

        if choice == '1':
            print('Создать папку')
            folder_name = input('Укажите имя папки: ')
            print(make_folder(folder_name))

        elif choice == '2':
            print('Удалить (файл/папку)')
            object_name = input('Укажите имя файла или папки: ')
            print(remove_file_or_folder(object_name))

        elif choice == '3':
            print('Копировать (файл/папку)')
            source = input('Укажите имя файла или папки для копирования: ')
            destination = input('Укажите путь, куда будем копировать: ')
            if os.path.exists(destination):
                if not confirmation(f'{destination} уже существует. Перезаписать? (да/нет): '):
                    print(f'{destination} уже существует. Перезапись запрещена')
            print(copy_file_or_folder(source, destination))

        elif choice == '4':
            print('Просмотреть содержимого рабочей директории')
            objets_list = list_dir()
            for item in objets_list:
                print(item)

        elif choice == '5':
            print('Посмотреть только папки')
            objets_list = list_dir(show_folders=True, show_files=False)
            for item in objets_list:
                print(item)

        elif choice == '6':
            print('Посмотреть только файлы')
            objets_list = list_dir(show_folders=False, show_files=True)
            for item in objets_list:
                print(item)

        elif choice == '8':
            print('Просмотр информации об операционной системе')
            for info_item in show_platform_info():
                print(info_item)

        elif choice == '9':
            print('Смена рабочей директории')
            new_directory = input('Укажите путь к новой рабочей директории: ')
            print(change_work_directory(new_directory))

        elif choice == '10':
            print('Выход')
            break

        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    run_file_manager()
