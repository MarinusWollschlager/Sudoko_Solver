from Header import Sudoko
import numpy as np


InitValues = np.array([[0, 0, 3, 0, 5, 0, 0, 7, 9],
                       [2, 0, 0, 6, 9, 3, 1, 5, 0],
                       [0, 8, 9, 0, 2, 1, 0, 0, 0],
                       [1, 0, 0, 0, 7, 8, 9, 0, 6],
                       [9, 0, 0, 2, 0, 0, 0, 0, 5],
                       [0, 2, 0, 0, 4, 0, 8, 0, 0],
                       [8, 0, 5, 0, 6, 2, 0, 9, 0],
                       [0, 9, 0, 5, 0, 7, 6, 0, 1],
                       [7, 0, 0, 4, 3, 0, 0, 8, 0]])


I = Sudoko(InitValues)
I.printInitTable()
I.solve()
I.printUpdatedTable()



