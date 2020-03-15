from collections import deque
import rubiks22


def solve(cube):
    que = deque([(cube, [])])
    cnt = 0
    while True:
        c, root = que.popleft()
        if c.solved():
            return root
            # print(*root)
            # exit()
        for op in ['D+', 'D-', 'F+', 'F-', 'R+', 'R-']:
            cc = c.copy()
            cc.rotate(op)
            que.append((cc, root + [op]))
        print(*root)


if __name__ == '__main__':
    cube = rubiks22.Cube()
    cube.shuffle(n=5)
    cube.show()
    print(solve(cube))