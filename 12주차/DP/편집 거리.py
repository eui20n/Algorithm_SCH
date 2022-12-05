def dp(word_1, word_2):
    length_word_1 = len(word_1)
    length_word_2 = len(word_2)

    dp_table = [[0 for _ in range(length_word_2 + 1)] for _ in range(length_word_1 + 1)]

    for idx in range(1, length_word_1 + 1):
        dp_table[idx][0] = idx

    for idx in range(1, length_word_2 + 1):
        dp_table[0][idx] = idx

    for x in range(1, length_word_1 + 1):
        for y in range(1, length_word_2 + 1):
            if word_1[x - 1] == word_2[y - 1]:
                dp_table[x][y] = dp_table[x - 1][y - 1]
            else:
                dp_table[x][y] = 1 + min(dp_table[x - 1][y], dp_table[x][y - 1], dp_table[x - 1][y - 1])
    return dp_table[length_word_1][length_word_2]


if __name__ == "__main__":
    word_1 = input()
    word_2 = input()
    print(dp(word_1, word_2))
