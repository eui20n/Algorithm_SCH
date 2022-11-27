def not_made_coin(arr):
    max_num = sum(arr)
    arr.sort()


if __name__ == '__main__':
    N = int(input())
    coins = list(map(int, input().split()))

    # not_made_coin(coins)

"""
[input]
5
3 2 1 1 9

[output]
8
"""
