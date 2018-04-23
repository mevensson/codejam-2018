from math import sqrt, floor, ceil

def clamp(x, minx, maxx):
    return min(max(x, minx), maxx)

def create_matrix(a):
    w = max(3, int(floor(sqrt(a))))
    h = max(3, int(ceil(float(a) / float(w))))
    m = [[False for x in range(w)] for y in range(h)]  # @UnusedVariable
    return (m, w, h) 

def num_empty_at_pos(m, x_pos, y_pos):
    num_empty = 0
    for x in range(x_pos - 1, x_pos + 2):
        for y in range(y_pos - 1, y_pos + 2):
            if not m[y][x]:
                num_empty += 1
    return num_empty

def find_best_pos(m, w, h):
    best_pos = (0, 0)
    best_num_empty = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            num_empty = num_empty_at_pos(m, x, y)
            if num_empty > best_num_empty:
                best_pos = (x, y)
                best_num_empty = num_empty
    return best_pos

def process_exchange(x, y):
    print("{} {}".format(x + 1, y + 1), flush=True)
    x, y = [int(s) for s in input().split()]
    if x == -1 and y == -1:
        exit()
    if x == 0 and y == 0:
        return "Done"
    return x - 1, y - 1 

def deploy_gopher(m, w, h):
    pos = find_best_pos(m, w, h)
    x = clamp(pos[0], 1, w - 2)
    y = clamp(pos[1], 1, h - 2)
    pos = process_exchange(x, y)
    if pos is "Done":
        return False
    x, y = pos
    m[y][x] = True
    return True

def main():
    t = int(input())
    for i in range(t):  # @UnusedVariable
        a = int(input())
        m, w, h = create_matrix(a)
        while deploy_gopher(m, w, h):
            pass

if __name__ == "__main__":
    main()
