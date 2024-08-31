def findDigits(n):

    d = [int(digit) for digit in str(n) if digit]

    count = 0
    for i in (d):
        if i != 0:
            if n % i == 0:
                count += 1
    print(count)
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        findDigits(n)