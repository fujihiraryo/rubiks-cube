import random


class Cube:
    def __init__(self,
                 u=['W', 'W', 'W', 'W'],
                 d=['Y', 'Y', 'Y', 'Y'],
                 f=['G', 'G', 'G', 'G'],
                 b=['B', 'B', 'B', 'B'],
                 l=['O', 'O', 'O', 'O'],
                 r=['R', 'R', 'R', 'R']):
        self.u = u
        self.d = d
        self.f = f
        self.b = b
        self.l = l
        self.r = r

    def copy(self):
        return Cube(self.u, self.d, self.f, self.b, self.l, self.r)

    def check(self):
        # ルービックキューブとしてありえるかどうか
        box = self.u + self.d + self.f + self.b + self.l + self.r
        return all([
            box.count('W') == 4,
            box.count('Y') == 4,
            box.count('G') == 4,
            box.count('B') == 4,
            box.count('O') == 4,
            box.count('R') == 4
        ])

    def show(self):
        print('    {} {}        '.format(self.u[0], self.u[1]))
        print('    {} {}        '.format(self.u[3], self.u[2]))
        print('{} {} {} {} {} {} {} {}'.format(self.l[0], self.l[1], self.f[0],
                                               self.f[1], self.r[0], self.r[1],
                                               self.b[0], self.b[1]))
        print('{} {} {} {} {} {} {} {}'.format(self.l[3], self.l[2], self.f[3],
                                               self.f[2], self.r[3], self.r[2],
                                               self.b[3], self.b[2]))
        print('    {} {}        '.format(self.d[0], self.d[1]))
        print('    {} {}        '.format(self.d[3], self.d[2]))

    def rotate(self, face):
        if face == 'D+':
            d = [self.d[3], self.d[0], self.d[1], self.d[2]]
            l = [self.l[0], self.l[1], self.b[2], self.b[3]]
            f = [self.f[0], self.f[1], self.l[2], self.l[3]]
            r = [self.r[0], self.r[1], self.f[2], self.f[3]]
            b = [self.b[0], self.b[1], self.r[2], self.r[3]]
            self.d = d
            self.l = l
            self.f = f
            self.r = r
            self.b = b
        if face == 'D-':
            d = [self.d[1], self.d[2], self.d[3], self.d[0]]
            l = [self.l[0], self.l[1], self.f[2], self.f[3]]
            f = [self.f[0], self.f[1], self.r[2], self.r[3]]
            r = [self.r[0], self.r[1], self.b[2], self.b[3]]
            b = [self.b[0], self.b[1], self.l[2], self.l[3]]
            self.d = d
            self.l = l
            self.f = f
            self.r = r
            self.b = b
        if face == 'F+':
            f = [self.f[3], self.f[0], self.f[1], self.f[2]]
            u = [self.u[0], self.u[1], self.l[1], self.l[2]]
            l = [self.l[0], self.d[0], self.d[1], self.l[3]]
            d = [self.r[3], self.r[0], self.d[2], self.d[3]]
            r = [self.u[3], self.r[1], self.r[2], self.u[2]]
            self.f = f
            self.u = u
            self.l = l
            self.d = d
            self.r = r
        if face == 'F-':
            f = [self.f[1], self.f[2], self.f[3], self.f[0]]
            u = [self.u[0], self.u[1], self.r[3], self.r[0]]
            l = [self.l[0], self.u[2], self.u[3], self.l[3]]
            d = [self.l[1], self.l[2], self.d[2], self.d[3]]
            r = [self.d[1], self.r[1], self.r[2], self.d[0]]
            self.f = f
            self.u = u
            self.l = l
            self.d = d
            self.r = r
        if face == 'R+':
            r = [self.r[3], self.r[0], self.r[1], self.r[2]]
            u = [self.u[0], self.f[1], self.f[2], self.u[3]]
            f = [self.f[0], self.d[1], self.d[2], self.f[3]]
            d = [self.d[0], self.b[3], self.b[0], self.d[3]]
            b = [self.u[2], self.b[1], self.b[2], self.u[1]]
            self.r = r
            self.u = u
            self.f = f
            self.d = d
            self.b = b
        if face == 'R-':
            r = [self.r[1], self.r[2], self.r[3], self.r[0]]
            u = [self.u[0], self.b[3], self.b[0], self.u[3]]
            f = [self.f[0], self.u[1], self.u[2], self.f[3]]
            d = [self.d[0], self.f[1], self.f[2], self.d[3]]
            b = [self.d[2], self.b[1], self.b[2], self.d[1]]
            self.r = r
            self.u = u
            self.f = f
            self.d = d
            self.b = b

    def solved(self):
        return all([
            self.u == ['W', 'W', 'W', 'W'], self.d == ['Y', 'Y', 'Y', 'Y'],
            self.f == ['G', 'G', 'G', 'G'], self.b == ['B', 'B', 'B', 'B'],
            self.l == ['O', 'O', 'O', 'O'], self.r == ['R', 'R', 'R', 'R']
        ])

    def shuffle(self, n=10):
        for i in range(n):
            self.rotate(random.choice(['D+', 'D-' 'F+', 'F-', 'R+', 'R-']))


if __name__ == '__main__':
    cube = Cube()
    cube.show()
    print('R+')
    cube.rotate('R+')
    cube.show()
    print('F+')
    cube.rotate('F+')
    cube.show()
    print('D-')
    cube.rotate('D-')
    cube.show()
    print('D+')
    cube.rotate('D+')
    cube.show()
    print('F-')
    cube.rotate('F-')
    cube.show()
    print('R-')
    cube.rotate('R-')
    cube.show()
