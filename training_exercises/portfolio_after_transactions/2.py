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