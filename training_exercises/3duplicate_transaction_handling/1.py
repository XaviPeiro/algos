'''
Exercise 3 — Duplicate Transaction Handling

Ideal time: 35–45 minutes
Good target: working happy path + duplicate handling in 30 minutes, edge cases/tests in the remaining 10–15 minutes.

Task

Write a function that processes portfolio transactions, but ensures that the same transaction ID is never applied twice.

You receive:

initial_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 10},
    {"account": "A1", "asset": "MSFT", "quantity": 5},
    {"account": "A2", "asset": "AAPL", "quantity": 7},
]
transactions = [
    {
        "id": "tx-001",
        "account": "A1",
        "asset": "AAPL",
        "type": "BUY",
        "quantity": 5,
    },
    {
        "id": "tx-002",
        "account": "A1",
        "asset": "MSFT",
        "type": "SELL",
        "quantity": 2,
    },
    {
        "id": "tx-001",
        "account": "A1",
        "asset": "AAPL",
        "type": "BUY",
        "quantity": 5,
    },
    {
        "id": "tx-003",
        "account": "A2",
        "asset": "AAPL",
        "type": "SELL",
        "quantity": 10,
    },
    {
        "id": "tx-004",
        "account": "A1",
        "asset": "GOOG",
        "type": "BUY",
        "quantity": 3,
    },
    {
        "id": "tx-002",
        "account": "A1",
        "asset": "MSFT",
        "type": "SELL",
        "quantity": 4,
    },
]
'''

BUY = 'BUY'
SELL = 'SELL'

class TransactionsError(Exception):
    ...


def are_trans_equal(a: dict, b: dict) -> bool:
    if set(a) != set(b):
        return False

    # This can be triky if nested or custom objets, but so far is okay
    for k in a:
        if a[k] != b[k]:
            return False

    return True

def clean_transactions(transactions: list[dict]):
    '''
    so far we just clean.
    but if repeated we should decide if cancel or criteria to pick one or another.

    ---
    - This is quite sensible
        - if duplicated
            - same data => good, apply one
            - diff data => cancel and inform
    '''
    new_transactions = []
    ids = set()
    error_ids = []

    for t  in transactions:
        if t['id'] in error_ids:
            error_ids.append(t['id'])
            continue

        if t['id'] not in ids:
            new_transactions.append(t)
            ids.add(t['id'])
            
        else:
            prev_duplciated = new_transactions[t['id']]
            if not are_trans_equal(t, prev_duplciated): # not perfect, should be done more carefully
                new_transactions.remove(t)
                error_ids.append(t['id'])

    if error_ids:
        raise TransactionsError(error_ids)

    return new_transactions


def reindex_positions_by_asset_and_account(transactions: list[dict]) -> dict:
    res = {}
    for t in transactions:
        res[(t['account'], t['asset'])] = t['quantity']

    return res


def process_transactions(transactions: list[dict], positions: list[dict]):
    nd_transactions = clean_transactions(transactions)
    positions: dict = reindex_positions_by_asset_and_account(nd_transactions)

    try:
        for t in nd_transactions:
            posid = (t['account'], t['asset'])

            if t['type'] == BUY:
                if posid not in posid:
                    positions[posid] = t['quantity']
                else:
                    positions[posid] += t['quantity']
            elif t['type'] == SELL:
                if posid not in positions or positions[posid] < t['quantity']:
                    raise TransactionsError(f'Not enough q for {posid}')
                else:
                    positions[posid] -= t['quantity']
    except KeyError as ky:
        raise TransactionsError('Transactions malformed') from k
    except Exception as ex:
        raise TransactionsError('something went wrong: unknown') from ex





if __name__ == '__main__':
    initial_positions = [
        {"account": "A1", "asset": "AAPL", "quantity": 10},
        {"account": "A1", "asset": "MSFT", "quantity": 5},
        {"account": "A2", "asset": "AAPL", "quantity": 7},
    ]
    transactions = [
        {
            "id": "tx-001",
            "account": "A1",
            "asset": "AAPL",
            "type": "BUY",
            "quantity": 5,
        },
        {
            "id": "tx-002",
            "account": "A1",
            "asset": "MSFT",
            "type": "SELL",
            "quantity": 2,
        },
        {
            "id": "tx-001",
            "account": "A1",
            "asset": "AAPL",
            "type": "BUY",
            "quantity": 5,
        },
        {
            "id": "tx-003",
            "account": "A2",
            "asset": "AAPL",
            "type": "SELL",
            "quantity": 10,
        },
        {
            "id": "tx-004",
            "account": "A1",
            "asset": "GOOG",
            "type": "BUY",
            "quantity": 3,
        },
        {
            "id": "tx-002",
            "account": "A1",
            "asset": "MSFT",
            "type": "SELL",
            "quantity": 4,
        },
    ]
    assert 4 == clean_transactions(transactions)
    process_transactions(transactions=transactions, positions=initial_positions) # No exceptions