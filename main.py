import rubiks22
*u, = input().split()
*d, = input().split()
*f, = input().split()
*b, = input().split()
*l, = input().split()
*r, = input().split()
cube = rubiks22.Cube(u, d, f, b, l, r)
cube.show()
