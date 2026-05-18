'''
Exercise 1 — Portfolio after transactions

Write a function that receives:

initial positions
a list of transactions
each transaction has account, asset, operation type, and quantity

Return the final positions after applying all valid transactions.

You decide the internal data structure, validation behavior, and return format.

Samples:
---
initial_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 10},
    {"account": "A1", "asset": "GOOG", "quantity": 5},
    {"account": "A2", "asset": "MSFT", "quantity": 20},
]

transactions = [
    {"account": "A1", "asset": "AAPL", "operation": "BUY", "quantity": 4},
    {"account": "A1", "asset": "GOOG", "operation": "SELL", "quantity": 2},
    {"account": "A2", "asset": "MSFT", "operation": "SELL", "quantity": 5},
    {"account": "A2", "asset": "TSLA", "operation": "BUY", "quantity": 7},
]
---
'''
from idlelib.iomenu import errors

from tasks.generic_algorithms.gcd import res

type ERRORS = list[dict]

def validate_positions(positions: list[dict]) -> tuple[bool, ERRORS]:
    # If 1 position or + is wrong -> FAIL; so the final state would be inconsistent
    req_fs = ['account', 'asset', 'quantity']
    errors: ERRORS = []
    for p in positions:
        missing_fields = []
        for f in req_fs:
            if f not in p:
                missing_fields.append(f)
        if missing_fields:
            errors.append({'position': p, 'code': '0', 'reason': 'missing-field', 'details': {'fields': missing_fields}})
            continue

        if p['quantity'] < 0: # could be <0 bc of short selling?
            errors.append({'position': p, 'code': '1', 'reason': 'invalid-quantity', 'details': {'quantity': p['quantity']}})

    # No need to add more for an interview
    return len(errors)<1, errors


def build_err(item: object, code: str, reason: str, details: dict) -> dict:
    return {'item': item, 'code': code, 'reason': reason, 'details': details}

def validate_transactions(transactions: list[dict], rt_valid: bool=False) -> tuple[bool, ERRORS, list[dict]|None]:
    errors: ERRORS = []
    valid_trans = [] if rt_valid else None
    for t in transactions:
        if t['quantity'] < 0:
            errors.append(build_err(t, '2', 'non valid q', {}))
        if t['operation'] not in ('BUY', 'SELL'):
            errors.append(build_err(t, '3', 'non valid operation', {}))

        if rt_valid:
            valid_trans.append(t)


    # No need to add more for an interview but:
    # Spot duplicateds
    return len(errors)<1, errors, valid_trans


type PF = dict
def setup_pf(positions: list[dict]) -> dict:
    return {(p['account'], p['asset']): p for p in positions}

def process_transactions(pf: PF, transactions: list[dict]) -> PF:
    for t in transactions:
        posid = (t['account'], t['asset'])
        if t['operations'] == 'BUY':
            if posid in pf:
                pf[posid]['quantity'] += t['quantity']
            else:
                pf[posid]['quantity'] = t['quantity']
        elif t['operations'] == 'SELL':
            if posid in pf:
                pf[posid]['quantity'] -= t['quantity']
            else:
                raise ValueError('Not enough assets')
        else:
            # transactions should have been already validated and IRL this would be entity that ensure data integrity
            raise ValueError('operations')

    return pf # acutally is updating in place, but well, this interface is better

def serialize_pf(pf: PF) -> dict:
    res = {}
    for posid in pf:
        acc, asset = posid[0], posid[1]

        if acc in res:
            res[acc]['asset'] = {asset: {'quantity': pf[posid]['quantity']}}

    return res

if __name__ == '__main__':
    initial_positions = [
        {"account": "A1", "asset": "AAPL", "quantity": 10},
        {"account": "A1", "asset": "GOOG", "quantity": 5},
        {"account": "A2", "asset": "MSFT", "quantity": 20},
    ]

    transactions = [
        {"account": "A1", "asset": "AAPL", "operation": "BUY", "quantity": 4},
        {"account": "A1", "asset": "GOOG", "operation": "SELL", "quantity": 2},
        {"account": "A2", "asset": "MSFT", "operation": "SELL", "quantity": 5},
        {"account": "A2", "asset": "TSLA", "operation": "BUY", "quantity": 7},
    ]
    # Validate data
    is_validp, pos_errs = validate_positions(initial_positions)
    is_validt, pos_trans, validt = validate_transactions(transactions)

    if is_validp:
        pf = setup_pf(initial_positions)
        upf = process_transactions(pf, transactions)
        response = serialize_pf(upf)
        # return {'pf': response, 'not_processable_transactions': pos_trans}
    else:
        # return {'not_processable_positions': pos_errs, 'not_processable_transactions': pos_trans}
        ...

