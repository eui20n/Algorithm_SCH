def solution(p):
    if not p:
        return ""

    p_1, p_2 = divide(p)

    if check(p_1):
        return p_1 + solution(p_2)

    else:
        answer = "("
        answer += solution(p_2)
        answer += ")"

        for word in p_2[1 : len(p_2) - 1]:
            if word == "(":
                answer += ")"
            else:
                answer += "("

        return answer


def divide(word):
    open_word = 0
    close_word = 0

    for idx in range(len(word)):
        if word[idx] == "(":
            open_word += 1
        else:
            close_word += 1

        if open_word == close_word:
            return word[:idx + 1], word[idx + 1:]


def check(word):
    stack = []

    for idx in range(len(word)):
        if word[idx] == "(":
            stack.append(word[idx])
        else:
            if not stack:
                return False
            stack.pop()

    return True


if __name__ == "__main__":
    p = "(()())()"
    print(solution(p))

