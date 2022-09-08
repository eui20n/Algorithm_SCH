def num_card_game():
    """ 숫자 카드 게임 """
    min_num = []
    for idx in range(R):
        min_num.append(min(board[idx]))

    return max(min_num)


def main():
    return num_card_game()


if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    print(main())

