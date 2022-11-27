def bowling_ball_select():
    result = 0
    for x in range(N - 1):
        player_1 = ball[x]
        for y in range(x + 1, N):
            player_2 = ball[y]
            if player_1 != player_2:
                result += 1

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    ball = list(map(int, input().split()))
    print(bowling_ball_select())
