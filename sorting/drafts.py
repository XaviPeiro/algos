def sort1(n: list[int]):
    # InsertionSort (Worst n2 -> Best 2n) avg(n*n/2)
    res = []
    res.append(n[0])
    for i in n[1:]:
        for k, v in enumerate(res):
            if v > i:
                break
        else:
            k+=1
        res.insert(k,i)

    return res


class QuickSort:
    def __call__(self, numbers: list[int]):
        ...

