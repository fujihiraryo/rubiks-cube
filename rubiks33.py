import numpy as np

class Cube33:
    # cp: corner permutation
    # co: corner orientation
    # ep: edge permutation
    # eo: edge orientation
    def __init__(self,
                 cp=[0, 1, 2, 3, 4, 5, 6, 7],
                 co=[0, 0, 0, 0, 0, 0, 0, 0],
                 ep=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                 eo=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
        self.cp = np.array(cp, dtype='int8')
        self.co = np.array(co, dtype='int8')
        self.ep = np.array(ep, dtype='int8')
        self.eo = np.array(eo, dtype='int8')

    def __eq__(self, obj):
        if isinstance(obj, Cube33):
            return all([
                (self.cp == obj.cp).all(),
                (self.co == obj.co).all(),
                (self.ep == obj.ep).all(),
                (self.eo == obj.eo).all()
            ])
        else:
            return False

    def solved(self):
        return self.__eq__(Cube33())

    def rotate(self, face):
        operations = {
            'U': Cube33(
                [3, 0, 1, 2, 4, 5, 6, 7],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ),
            'D': Cube33(
                [0, 1, 2, 3, 5, 6, 7, 4],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ),
            'L': Cube33(
                [4, 1, 2, 0, 7, 5, 6, 3],
                [2, 0, 0, 1, 1, 0, 0, 2],
                [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ),
            'R': Cube33(
                [0, 2, 6, 3, 4, 1, 5, 7],
                [0, 1, 2, 0, 0, 2, 1, 0],
                [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ),
            'F': Cube33(
                [0, 1, 3, 7, 4, 5, 2, 6],
                [0, 0, 1, 2, 0, 0, 2, 1],
                [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]
            ),
            'B': Cube33(
                [1, 5, 2, 3, 0, 4, 6, 7],
                [1, 2, 0, 0, 2, 1, 0, 0],
                [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
                [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
            )
        }
        state = operations[face]
        self.cp = self.cp[state.cp]
        self.co = (self.co[state.cp] + state.co) % 3
        self.ep = self.ep[state.ep]
        self.eo = (self.eo[state.ep] + state.eo) % 2

    def show(self):
        print('cp : {}'.format(self.cp))
        print('co : {}'.format(self.co))
        print('ep : {}'.format(self.ep))
        print('eo : {}'.format(self.eo))


if __name__ == '__main__':
    cube = Cube33()
    # print(cube.solved())
    # cube.rotate('R')
    # print(cube.solved())
    # cube.rotate('R')
    # print(cube.solved())
    # cube.rotate('R')
    # print(cube.solved())
    # cube.rotate('R')
    # print(cube.solved())
    print(cube.show())
