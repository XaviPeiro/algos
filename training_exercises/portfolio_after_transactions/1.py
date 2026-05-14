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

from dataclasses import dataclass
from typing import Self

type posint = int
@dataclass
class Transaction:
    account: str
    asset: str # 3 or 4 len
    operation: str # BUY or SELL
    quantity: posint # >0
    failed: bool = False

    @classmethod
    def build_from_dict(cls, transaction: dict) -> list[Self]:
        ...

def merge_positions_by_user(initial_positions: list[dict]) -> dict:
    mpos = {}

    for p in initial_positions:
        if p["account"] not in mpos:
            mpos[p["account"]] = {"assets": {}}
        mpos[p["account"]]["assets"][p["asset"]] = mpos[p["account"]]["assets"].get(p["asset"],0) + p["quantity"]

    return mpos



class TransactionsProcessor:
    def __init__(self, initial_positions: list[dict]):
        self.positions: dict = merge_positions_by_user(initial_positions)

    def __call__(self, raw_transactions: list[dict]):
        '''
        1.- Validate transactions -> done by the entity
        Constraints:
        - positions cannot be negative -> cannot sell more than it has
        - as long as we do not know the buyer and seller, we cannot check integrity
        - each transaction is independent
        - they should be concurrent
        - if there is one valid order, then it should work
        '''
        transactions: list[Transaction] = Transaction.build_from_dict(raw_transactions)
        all_failed: bool|None = None
        while all_failed is None or not all_failed:
            all_failed = None
            for transaction in transactions:
                acc_asset_q = self.positions.get(transaction.account, {}).get(transaction.asset).get('quantity', 0)
                if transaction.operation == "SELL":
                    if acc_asset_q < transaction.quantity:
                        transaction.failed = True

                        all_failed = True if all_failed is None else (all_failed and True)
                    else:
                        self.positions[transaction.account][transaction.asset]['quantity'] -= transaction.quantity

                if transaction.operation == "BUY":
                    self.positions[transaction.account][transaction.asset]['quantity'] += transaction.quantity

        return self.positions








