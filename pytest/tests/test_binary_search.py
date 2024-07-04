from functions.binary_search import binary_search

def test_binary_search():
    test_nums_1 = [-3, 2, 3, 8, 10, 10000]
    assert binary_search(nums=test_nums_1, target=3) == 2
    assert binary_search(nums=test_nums_1, target=-3) == 0
    assert binary_search(nums=test_nums_1, target=10000) == 5
    assert binary_search(nums=test_nums_1, target=11) == -1

    test_nums_2 = [6, 11, 19, 20, 21]
    assert binary_search(nums=test_nums_2, target=11) == 1
    assert binary_search(nums=test_nums_2, target=6) == 0
    assert binary_search(nums=test_nums_2, target=21) == 4
    assert binary_search(nums=test_nums_2, target=18) == -1

    test_nums_3 = []
    assert binary_search(nums=test_nums_3, target=6) == -1

    test_nums_4 = [i for i in range(1000)]
    assert binary_search(nums=test_nums_4, target=18) == 18
    assert binary_search(nums=test_nums_4, target=999) == 999
    assert binary_search(nums=test_nums_4, target=0) == 0
    assert binary_search(nums=test_nums_4, target=-18) == -1