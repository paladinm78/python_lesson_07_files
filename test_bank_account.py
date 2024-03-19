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
