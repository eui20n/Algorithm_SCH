def resort(arr):
    num = []
    alphabet = []

    for x in arr:
        if x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "0":
            num.append(int(x))
        else:
            alphabet.append(x)

    alphabet.sort()
    result = alphabet + list(str(sum(num)))
    return result


if __name__ == "__main__":
    word = list(input())
    ans = resort(word)
    print(*ans, sep="")
