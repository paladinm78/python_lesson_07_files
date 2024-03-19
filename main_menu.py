from bank_account import run_bank_account
from file_manager import run_file_manager


def show_menu():
    print()
    print('Главное меню:')
    print('1. консольный файловый менеджер')
    print('2. мой банковский счет')
    print('3. создатель программы')
    print('4. выход')
    print()


def show_creator():
    return 'Alexander Melikhov'


def run_main():

    while True:
        show_menu()
        choice = input('Выберите пункт меню: ')
        print()

        if choice == '1':
            run_file_manager()

        elif choice == '2':
            run_bank_account()

        elif choice == '3':
            print('Создатель программы')
            print(show_creator())

        elif choice == '4':
            print('Выход')
            break

        else:
            print('Неверный пункт меню')

        # print()
        # input('Для возврата в главное меню нажмите Enter')

if __name__ == "__main__":
    run_main()

