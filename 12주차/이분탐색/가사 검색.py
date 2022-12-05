from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reverse_arr = [[] for _ in range(10001)]

    for word in words:
        word_length = len(word)
        arr[word_length].append(word)
        reverse_arr[word_length].append(word[::-1])

    for idx in range(10001):
        arr[idx].sort()
        reverse_arr[idx].sort()

    for query in queries:
        query_length = len(query)
        if query[0] != "?":
            result = count_by_range(arr[query_length], query.replace("?", "a"), query.replace("?", "z"))
        else:
            result = count_by_range(reverse_arr[query_length], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
        answer.append(result)
    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
