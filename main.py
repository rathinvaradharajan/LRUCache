from LRUCache import LRUCache


def test_lru_cache():
    cache = LRUCache(1)
    assert cache.get(6) == -1
    assert cache.get(8) == -1
    cache.put(12, 1)
    assert cache.get(2) == -1
    cache.put(15, 11)
    cache.put(5, 2)
    cache.put(1, 15)
    cache.put(4, 2)
    assert cache.get(5) == -1
    cache.put(15, 15)

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_lru_cache()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
