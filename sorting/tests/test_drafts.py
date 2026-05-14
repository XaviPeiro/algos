import random

import pytest
from sorting.drafts import sort1

@pytest.fixture(scope="session")
def dataset_tests():
    t = [
        [random.randint(0, 100) for x in range(100)],
        [1,1,2,2,3],
        [x for x in  range(100, -1, -1)],
        [3,3,2,2,1]
    ]
    return t

def test_sort1(dataset_tests: list):
    for x in dataset_tests:
        assert list(sorted(x)) == sort1(x)

