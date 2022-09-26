def main():
    A_arr.sort()
    B_arr.sort(reverse=True)

    for idx in range(K):
        if A_arr[idx] > B_arr[idx]:
            break

        A_arr[idx], B_arr[idx] = B_arr[idx], A_arr[idx]

    print(sum(A_arr))


if __name__ == '__main__':
    N, K = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    main()
