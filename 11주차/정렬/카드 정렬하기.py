import heapq


def main():
    cards = []
    result = 0

    for card in card_sizes:
        heapq.heappush(cards, card)

    while True:
        if len(cards) == 1:
            return max(result, 0)

        card_1 = heapq.heappop(cards)
        card_2 = heapq.heappop(cards)

        temp = card_1 + card_2
        result += temp

        heapq.heappush(cards, temp)


if __name__ == "__main__":
    N = int(input())
    card_sizes = []
    for _ in range(N):
        card_size = int(input())
        card_sizes.append(card_size)
    card_sizes.sort()

    print(main())

