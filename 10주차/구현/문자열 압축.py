def solution(arr):
    result = len(arr)

    for step in range(1, len(arr) // 2 + 1):
        compressed = ""
        prev = arr[0:step]
        count = 1

        for j in range(step, len(arr), step):
            if prev == arr[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = arr[j:j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev

        result = min(result, len(compressed))

    return result


if __name__ == "__main__":
    word = "aabbaccc"
    print(solution(word))
