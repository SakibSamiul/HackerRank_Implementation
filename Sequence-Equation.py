def permutationEquation(p):
    # Write your code here
    value = []
    for i in p:
        for x in range(1, n+1):
            if p[i] == x:
                value.append(x)
    for v in value:
        print(v)

if __name__ == '__main__':
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)