def guild(arr):
    adventurer = {}
    result = 0

    for idx in arr:
        if idx not in adventurer.keys():
            adventurer[idx] = 1
        else:
            adventurer[idx] += 1

    for key in adventurer.keys():
        if adventurer[key] >= key:
            result = max(result, key)

    return result


if __name__ == '__main__':
    N = int(input())
    phobia = list(map(int, input().split()))
    print(guild(phobia))

"""
[input]
5
2 3 1 2 2
[output]
2
"""