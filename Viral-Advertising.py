def viralAdvertising(n):
    # Write your code here
    Shared = 5
    Cumulative = 0
    for _ in range(1, n + 1):

        liked = (Shared // 2)
        Cumulative += liked
        Shared = liked * 3
    print(Cumulative)

if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)
