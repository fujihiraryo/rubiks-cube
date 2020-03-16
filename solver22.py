from collections import deque
import rubiks22


def solve(cube):
    que = deque([(cube, [])])
    cnt = 0
    while True:
        c, root = que.popleft()
        if c.solved():
            return root
        for op in ['D', 'F', 'R']:
            for cnt in range(1, 3 + 1):
                cc = c.copy()
                cc.rotate(op, cnt=cnt)
                que.append((cc, root + [op + str(cnt)]))
        print(*root)


if __name__ == '__main__':
    cube = rubiks22.Cube()
    cube.shuffle(n=20)
    cube.show()
    print(*solve(cube))