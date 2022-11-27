def main(arr):
    arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
    return arr


if __name__ == '__main__':
    N = int(input())
    students = []
    for _ in range(N):
        name, korean_score, english_score, math_score = map(str, input().split())
        students.append([name, int(korean_score), int(english_score), int(math_score)])

    result = main(students)

    for idx in range(N):
        print(result[idx][0])