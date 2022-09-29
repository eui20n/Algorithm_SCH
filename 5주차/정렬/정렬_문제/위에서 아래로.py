def main():
    arr.sort()
    for num in arr:
        print(num, end=" ")


if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        num = int(input())
        arr.append(num)

    main()
