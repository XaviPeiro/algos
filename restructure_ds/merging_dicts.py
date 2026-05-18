initial_positions = [
    {"account": "A1", "asset": "AAPL", "quantity": 10},
    {"account": "A1", "asset": "MSFT", "quantity": 5},
    {"account": "A2", "asset": "GOOG", "quantity": 8},
    {"account": "A2", "asset": "TSLA", "quantity": 3},
]

def to_single_dict(ld: list[dict]) -> dict:
    return {
        r[0]: r[1]
        for r in map(
            lambda x: ((x['account'], x['asset']), x['quantity']),
            initial_positions
        )
    }

def to_single_dict(ld: list[dict]) -> dict:
    return {
        (x['account'], x['asset']): x['quantity'] for x in initial_positions
    }