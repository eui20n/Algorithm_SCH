def big_num_role():
    """ 큰수의 법칙 """
    num.sort(reverse=True)
    end_con = 0
    result = 0
    cnt = 0
    while True:
        if end_con == M:
            return result

        if cnt <= K:
            result += num[0]
        else:
            result += num[1]
            cnt = 0

        end_con += 1


def main():
    print(big_num_role())


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    num = list(map(int, input().split()))
    main()