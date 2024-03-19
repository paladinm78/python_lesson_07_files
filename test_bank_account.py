import os
import pickle
import bank_account as ba


def test_prepare_history_record():
    history_record = ba.prepare_history_record(10, 'desc', 100)
    assert history_record['value'] == 10
    assert history_record['description'] == 'desc'
    assert history_record['balance'] == 100


def test_get_record_data():
    history_record = {'value': 10, 'description': 'desc', 'balance': 100}
    value, description, balance = ba.get_record_data(history_record)
    assert value == 10
    assert description == 'desc'
    assert balance == 100


def test_load_account_data():
    test_load_account_data_file = 'test_load_account_data.data'
    account_history = [ba.prepare_history_record(100, 'Пополнение счета', 100),
                       ba.prepare_history_record(-10, 'test', 90)]
    account_balance = 90
    with open(test_load_account_data_file, 'wb') as f:
        pickle.dump(account_history, f)

    test_account_balance, test_account_history = ba.load_account_data(test_load_account_data_file)

    assert test_account_balance == account_balance
    assert test_account_history == account_history

    os.remove(test_load_account_data_file)


def test_save_account_history():
    test_save_account_history_file = 'test_save_account_history.data'
    account_history = [ba.prepare_history_record(100, 'Пополнение счета', 100),
                       ba.prepare_history_record(-10, 'test', 90)]
    account_balance = 90

    ba.save_account_history(account_history, test_save_account_history_file)

    test_account_history = []
    test_account_balance = 0

    if os.path.exists(test_save_account_history_file):
        with open(test_save_account_history_file, 'rb') as f:
            test_account_history = pickle.load(f)

        for history_record in test_account_history:
            value, _, _ = ba.get_record_data(history_record)
            test_account_balance += value

    assert test_account_balance == account_balance
    assert test_account_history == account_history

    os.remove(test_save_account_history_file)
