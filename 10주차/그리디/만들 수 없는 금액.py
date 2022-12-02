def not_made_coin(arr):
    arr.sort()

    temp = 1

    for x in arr:
        if temp < x:
            break

        temp += x

    print(temp)


if __name__ == '__main__':
    N = int(input())
    coins = list(map(int, input().split()))

    not_made_coin(coins)

"""
[input]
5
3 2 1 1 9

[output]
8
"""
