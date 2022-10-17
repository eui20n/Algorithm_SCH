def dp():
    dp_table = [[float('inf') for _ in range(M + 1)] for _ in range(N)]





if __name__ == '__main__':
    N, M = map(int, input().split())
    dollars = [0]
    for _ in range(N):
        temp = int(input())
        dollars += [temp]

    print(dp())

# 배낭 문제의 응용