from restructure_ds.merging_dicts import to_single_dict


def test_to_single_dict():
    initial_positions = [
        {"account": "A1", "asset": "AAPL", "quantity": 10},
        {"account": "A1", "asset": "MSFT", "quantity": 5},
        {"account": "A2", "asset": "GOOG", "quantity": 8},
        {"account": "A2", "asset": "TSLA", "quantity": 3},
    ]
    r = to_single_dict(initial_positions)
    assert len(r) == 4
    assert ('A1', "AAPL") in r
    assert ('A1', "MSFT") in r
    assert ('A2', "GOOG") in r
    assert ('A2', "TSLA") in r