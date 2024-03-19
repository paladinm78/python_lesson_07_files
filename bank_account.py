"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета.
При выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму, она добавляется к счету
снова попадаем в основное меню

2. покупка.
При выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок.
Выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход.
Выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import pickle
from input_functions import input_correct_float


ACCOUNT_HISTORY_FILE_NAME = 'account_history.data'


def prepare_history_record(value, description, balance):
    return {'value': value, 'description': description, 'balance': balance}


def get_record_data(record):
    return record['value'], record['description'], record['balance']


def load_account_data(data_file=ACCOUNT_HISTORY_FILE_NAME):

    account_history = []
    account_balance = 0

    if os.path.exists(data_file):
        with open(data_file, 'rb') as f:
            account_history = pickle.load(f)

        for history_record in account_history:
            value, _, _ = get_record_data(history_record)
            account_balance += value

    return account_balance, account_history


def save_account_history(account_history, data_file=ACCOUNT_HISTORY_FILE_NAME):
    with open(data_file, 'wb') as f:
        pickle.dump(account_history, f)


def show_bank_account_menu(account_balance):
    print()
    print('Мой банковский счет')
    print()
    print(f'Мой баланс: {account_balance:.2f}')
    print()
    print('Меню:')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история счета')
    print('4. выход')
    print()


def run_bank_account():
    account_balance, account_history = load_account_data()
    while True:
        show_bank_account_menu(account_balance)
        choice = input('Выберите пункт меню: ')
        print()
        if choice == '1':
            print('Пополнение счета.')
            add_sum = input_correct_float('Укажите сумму на которую необходимо пополнить счет: ')
            account_balance += add_sum
            account_history.append(prepare_history_record(add_sum, 'Пополнение счета', account_balance))
        elif choice == '2':
            print('Покупка.')
            buy_sum = input_correct_float('Укажите сумму покупки: ')
            if buy_sum <= account_balance:
                buy_name = input('Укажите название покупки: ')
                account_balance -= buy_sum
                account_history.append(prepare_history_record(-buy_sum, buy_name, account_balance))
            else:
                print('Денег на счету не хватает!')
        elif choice == '3':
            print('История счета.')
            print()
            for history_record in account_history:
                value, description, balance = get_record_data(history_record)
                print(f'Сумма: {value:>8.2f}, Операция: {description:<18}, Остаток: {balance:>8.2f}')
        elif choice == '4':
            print('Выход.')
            save_account_history(account_history)
            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    run_bank_account()
