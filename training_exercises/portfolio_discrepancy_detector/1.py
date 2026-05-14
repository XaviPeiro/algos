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