def trouble_sort(l):
    done = False
    while not done:
        done = True
        for i in range(0, len(l) - 2):
            if l[i] > l[i + 2]:
                done = False
                l[i], l[i + 2] = l[i + 2], l[i]

def check_trouble_sort(l):
    trouble_sort(l)
    for i in range(0, len(l) - 1):
        if l[i + 1] < l[i]:
            return i
    return "OK"

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        all_l = input().split()
        l = [int(all_l[i]) for i in range(n)]
        result = check_trouble_sort(l)
        print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
    main()
