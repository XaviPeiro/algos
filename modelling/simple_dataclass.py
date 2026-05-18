from dataclasses import dataclass, field
from typing import Self
from enum import Enum, StrEnum

class TOps(StrEnum):
    BUY = 'BUY'
    SELL = "SELL"

@dataclass
class Transaction:
    quantity: int
    operation: TOps
    asset: str
    account: str

    def __post_init__(self):
        ...

    @classmethod
    def create_list(cls, raw_transactions: list[dict]) -> list[Self]:
        res: list[Self] = []
        for t in raw_transactions:
            res.append(cls(**t))

        return res


if __name__ == '__main__':
    transactions = [
        {"account": "A1", "asset": "AAPL", "operation": "BUY", "quantity": 4},
        {"account": "A1", "asset": "GOOG", "operation": "SELL", "quantity": 2},
        {"account": "A2", "asset": "MSFT", "operation": "SELL", "quantity": 5},
        {"account": "A2", "asset": "TSLA", "operation": "BUY", "quantity": 7},
    ]

    transactions = Transaction.create_list(transactions)
    assert len(transactions) == 4
    for t in transactions:
        assert isinstance(t, Transaction)
        assert t.account
        assert t.asset
        assert t.operation
        assert t.quantity

    print(transactions)


