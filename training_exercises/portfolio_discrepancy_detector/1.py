'''
Expected time 40-50 min
Goal:
Write a function that receives:

day_zero_positions
transactions
reported_day_one_positions

It should compute what the day-one positions should be, then compare them with the reported day-one positions and return the discrepancies.

Do not just compare day zero vs day one directly. You must apply the transactions first.

day_zero_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 10},
    {"account": "A1", "asset": "GOOG", "quantity": 5},
    {"account": "A2", "asset": "TSLA", "quantity": 3},
    {"account": "A2", "asset": "MSFT", "quantity": 8},
]

transactions = [
    {"account": "A1", "asset": "AAPL", "type": "BUY", "quantity": 5},
    {"account": "A1", "asset": "GOOG", "type": "SELL", "quantity": 2},
    {"account": "A2", "asset": "TSLA", "type": "SELL", "quantity": 1},
    {"account": "A2", "asset": "AMZN", "type": "BUY", "quantity": 4},
]

reported_day_one_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 15},
    {"account": "A1", "asset": "GOOG", "quantity": 4},
    {"account": "A2", "asset": "TSLA", "quantity": 2},
    {"account": "A2", "asset": "MSFT", "quantity": 8},
    {"account": "A2", "asset": "AMZN", "quantity": 5},
    {"account": "A3", "asset": "NFLX", "quantity": 7},
]
'''
from collections import defaultdict

day_zero_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 10},
    {"account": "A1", "asset": "GOOG", "quantity": 5},
    {"account": "A2", "asset": "TSLA", "quantity": 3},
    {"account": "A2", "asset": "MSFT", "quantity": 8},
]

transactions = [
    {"account": "A1", "asset": "AAPL", "type": "BUY", "quantity": 5},
    {"account": "A1", "asset": "GOOG", "type": "SELL", "quantity": 2},
    {"account": "A2", "asset": "TSLA", "type": "SELL", "quantity": 1},
    {"account": "A2", "asset": "AMZN", "type": "BUY", "quantity": 4},
]

reported_day_one_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 15},
    {"account": "A1", "asset": "GOOG", "quantity": 4},
    {"account": "A2", "asset": "TSLA", "quantity": 2},
    {"account": "A2", "asset": "MSFT", "quantity": 8},
    {"account": "A2", "asset": "AMZN", "quantity": 5},
    {"account": "A3", "asset": "NFLX", "quantity": 7},
]

def positions_by_user_and_asset(positions: list[dict]) -> dict:
    res = {}
    # a = {x:1 for x in map(lambda x: {(x['account'], x['asset'])}, positions))}
    for p in positions:
        res[(p['account'], p['asset'])] = {'quantity': p['quantity']}

    return res

class InvalidTransactions(Exception):
    ...

def compare_positions(a: dict, b: dict) -> tuple[bool, list[str]]:
    errors = []
    res: bool = True
    if len(a) != len(b):
        res = False
        errors.append(f'First has {len(a)} elements while 2nd has {len(b)}')
    for k in a:
        try:
            b_v = b[k]
        except KeyError:
            res = False
            errors.append(f'{k} is not present in the second positions')

        if a[k] != b_v:
            res = False
            errors.append(f'for {k}, values differ {a[k]} != {b_v}')

    return res, errors


def process_transactions(d0_positions: list[dict], transactions: list[dict]):
    '''
    We assume if one transactions is invalid then the whole set it is.

    '''
    updated_position = positions_by_user_and_asset(d0_positions)
    for t in transactions:
        if t['type'] == 'BUY':
            if (t['account'], t['asset']) not in updated_position:
                updated_position[(t['account'], t['asset'])] = {'quantity': t['quantity']}
            else:
                updated_position[(t['account'], t['asset'])]['quantity'] += t['quantity']

        elif t['type'] == 'SELL':
            try:
                acc_asset_q = updated_position[(t['account'], t['asset'])]['quantity']
            except KeyError:
                raise InvalidTransactions

            if acc_asset_q < t['quantity']:
                raise InvalidTransactions

            updated_position[(t['account'], t['asset'])]['quantity'] -= t['quantity']

    return updated_position


if __name__ == "__main__":
    updated_position = process_transactions(day_zero_positions, transactions)
    indexed_d1_positions = positions_by_user_and_asset(reported_day_one_positions)
    r = compare_positions(updated_position, indexed_d1_positions)
    print(compare_positions(updated_position, indexed_d1_positions))
    assert True in compare_positions(updated_position, indexed_d1_positions)
