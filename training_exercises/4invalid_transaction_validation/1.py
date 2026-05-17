'''
Exercise 4 — Invalid transaction validation

Ideal time: 35–45 minutes
Hard limit: 60 minutes

Write a function that processes an initial portfolio and a list of transactions.

The function should:

Apply only valid transactions.
Reject invalid transactions.
Return the final portfolio state.
Return enough information to inspect which transactions were rejected.

You decide the exact return format.

initial_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 10},
    {"account": "A1", "asset": "MSFT", "quantity": 5},
    {"account": "A2", "asset": "GOOG", "quantity": 8},
    {"account": "A2", "asset": "TSLA", "quantity": 3},
]
transactions = [
    {
        "id": "T1",
        "account": "A1",
        "asset": "AAPL",
        "operation": "BUY",
        "quantity": 5,
    },
    {
        "id": "T2",
        "account": "A1",
        "asset": "MSFT",
        "operation": "SELL",
        "quantity": 2,
    },
    {
        "id": "T3",
        "account": "A2",
        "asset": "GOOG",
        "operation": "SELL",
        "quantity": 10,
    },
    {
        "id": "T4",
        "account": "A2",
        "asset": "TSLA",
        "operation": "TRANSFER",
        "quantity": 1,
    },
    {
        "id": "T5",
        "account": "A3",
        "asset": "NFLX",
        "operation": "BUY",
        "quantity": 4,
    },
    {
        "id": "T6",
        "account": "A1",
        "asset": "AAPL",
        "operation": "BUY",
        "quantity": -3,
    },
    {
        "id": "T7",
        "account": "",
        "asset": "MSFT",
        "operation": "BUY",
        "quantity": 1,
    },
    {
        "id": "T8",
        "account": "A1",
        "operation": "SELL",
        "quantity": 1,
    },
]
'''

class TransactionError(Exception):
    ...

def validate_transactions(transactions: list[dict]) -> list:

    seen_ids = set()
    n_trans = {}
    errors = []
    for t in transactions:
        if t['id'] in seen_ids:
            if n_trans[t['id']] == t:
                errors.append({'code':'DUPLCIATED', 'trans': t})
            else:
                errors.append({'code':'CONFLICT', 'trans': [t, n_trans[t['id']]]})
            continue

        if t['quantity'] < 0:
            errors.append({'code':'INVLAID_QUANTITY', 'trans': t})
        seen_ids.add(t['id'])
        n_trans[t['id']] = t

    return errors

def validate_positions(positions: list[dict]) -> list:
    res = []
    return res

def setup_portfolio(positions: list[dict]) -> dict:
    pf = {}
    for p in positions:
        posid = (p['account'], p['asset'])
        if posid not in pf:
            pf[posid] = p['quantity']
        else:
            pf[posid] += p['quantity']

    return pf

type PortfolioExecution = dict
def update_portfolio(positions: list[dict], transactions: list[dict]) -> PortfolioExecution:
    pf = setup_portfolio(positions=positions)
    errors = []
    pf_execution = {'pf': pf, 'errors': errors}

    for t in transactions:
        posid = (t['account'], t['asset'])
        if t['operation'] == 'BUY':
            if posid in pf:
                pf[posid] += t['quantity']
            else:
                pf[posid] = t['quantity']
        elif t['operation'] == 'SELL':
            if posid not in pf:
                errors.append({'sell': t, 'owning': 0, 'code': 0, 'posid': posid})

            if pf[posid] < t['quantity']:
                errors.append({'sell': t, 'owning': t['quantity'], 'code': 0, 'posid': posid})

    return pf_execution


def main(positions: list[dict], transactions: list[dict]):
    positions_errs = validate_positions()
    transactions_errs = validate_transactions()

    if positions_errs or transactions_errs:
        return positions_errs, transactions_errs

if __name__ == '__main__':
    initial_positions = [
        {"account": "A1", "asset": "AAPL", "quantity": 10},
        {"account": "A1", "asset": "MSFT", "quantity": 5},
        {"account": "A2", "asset": "GOOG", "quantity": 8},
        {"account": "A2", "asset": "TSLA", "quantity": 3},
    ]
    transactions = [
        {
            "id": "T1",
            "account": "A1",
            "asset": "AAPL",
            "operation": "BUY",
            "quantity": 5,
        },
        {
            "id": "T2",
            "account": "A1",
            "asset": "MSFT",
            "operation": "SELL",
            "quantity": 2,
        },
        {
            "id": "T3",
            "account": "A2",
            "asset": "GOOG",
            "operation": "SELL",
            "quantity": 10,
        },
        {
            "id": "T4",
            "account": "A2",
            "asset": "TSLA",
            "operation": "TRANSFER",
            "quantity": 1,
        },
        {
            "id": "T5",
            "account": "A3",
            "asset": "NFLX",
            "operation": "BUY",
            "quantity": 4,
        },
        {
            "id": "T6",
            "account": "A1",
            "asset": "AAPL",
            "operation": "BUY",
            "quantity": -3,
        },
        {
            "id": "T7",
            "account": "",
            "asset": "MSFT",
            "operation": "BUY",
            "quantity": 1,
        },
        {
            "id": "T8",
            "account": "A1",
            "operation": "SELL",
            "quantity": 1,
        },
    ]
    main(positions=initial_positions, transactions=transactions)