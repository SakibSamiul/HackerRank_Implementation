def appendAndDelete(s, t, k):

    if k >= (len(s) + len(t)):
        print("Yes")
    
    mark = min(len(s), len(t))
    index = min(len(s), len(t))

    for i in range(0, index):
        if s[i] != t[i]:
            mark = i
            break

    k -= (len(s) - mark)
    k -= (len(t) - mark)

    if k >= 0 and k % 2 == 0:
        print("Yes")
    else:
        print("No")
    
if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    appendAndDelete(s, t, k)
