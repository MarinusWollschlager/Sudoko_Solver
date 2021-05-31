import numpy as np
from tabulate import tabulate


class Sudoko:
    def __init__(self, InitTable):
        self._initTable = InitTable
        self._TableUpdated = self._initTable
        self._initCoord = np.argwhere(self._initTable == 0)
        self._possibleValues = {str(k):[1, 2, 3, 4, 5, 6, 7, 8, 9] for k in self._initCoord}
        self._Index = {0: [0, 3], 1: [0, 3], 2: [0, 3],
                       3: [3, 6], 4: [3, 6], 5: [3, 6],
                       6: [6, 9], 7: [6, 9], 8: [6, 9]}

    def TableUpdate(self, RowIndex, ColumnIndex, Digit):
        #update whole table and Dict with quadrants
        self._TableUpdated[RowIndex, ColumnIndex] = Digit

    def RowCheck(self, RowIndex, Digit):
        # return True if Digit is in Row, False if Digit is not in Row
        return Digit in self._TableUpdated[RowIndex, :]

    def ColumnCheck(self, ColumnIndex, Digit):
        # return True if Digit in in Column, False if Digit is not in Column
        return Digit in self._TableUpdated[:, ColumnIndex]

    def QuadrantCheck(self, RowIndex, ColumnIndex, Digit):
        # return True if Digit in in Quadrant, False if Digit is not in Quadrant
        return Digit in self._TableUpdated[min(self._Index[RowIndex]) : max(self._Index[RowIndex]),
                                            min(self._Index[ColumnIndex]) : max(self._Index[ColumnIndex])]

    def PlausiCheck(self, rowIndex, columnIndex, Digit, List):
        if not (self.QuadrantCheck(rowIndex, columnIndex, Digit) or self.RowCheck(rowIndex, Digit) or self.ColumnCheck(columnIndex, Digit)):
            List.append(Digit)

    def printInitTable(self):
        # print self._initTable
        print("Initial Sudoko: \n {}".format(tabulate(self._initTable)))

    def printUpdatedTable(self):
        # print self._initTable
        print("Updated Sudoko: \n {}".format(tabulate(self._TableUpdated)))

    def solve(self):
        while np.all(self._TableUpdated) == False:
            for Position, Values in self._possibleValues.items():
                rowIndex, columnIndex = int(Position[1]), int(Position[3])

                # sammelt alle möglichen Werte für diese Position
                possibleDigits = []
                for Digit in Values:
                    self.PlausiCheck(rowIndex, columnIndex, Digit, possibleDigits)
                self._possibleValues[Position] = possibleDigits

                # aktualisiert Wert wenn nur einer möglich ist und QuadrantQueck erfolgreich
                if len(Values) == 1 and not self.QuadrantCheck(rowIndex, columnIndex, Values[0]):
                    self.TableUpdate(rowIndex, columnIndex, Values[0])



