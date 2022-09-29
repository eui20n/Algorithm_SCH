def main():
    score.sort(key=lambda x: int(x[1]))
    for idx in range(N):
        print(score[idx][0], end=" ")


if __name__ == '__main__':
    N = int(input())
    score = [list(map(str, input().split())) for _ in range(N)]
    main()
