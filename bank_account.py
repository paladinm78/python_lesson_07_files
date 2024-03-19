import os
import pickle
from input_functions import input_correct_float


def prepare_history_record(value, description, balance):
    return {'value': value, 'description': description, 'balance': balance}


def get_record_data(record):
    return record['value'], record['description'], record['balance']


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
    account_balance, account_history = (0, [])
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
            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    run_bank_account()
