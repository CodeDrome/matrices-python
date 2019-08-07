
class Matrix:

    def __init__(self, entries=None, rowcount=0, columncount=0):

        """
        Create a Matrix object either with the supplied values
        or with the specified number of rows and columns of 0 values.
        """

        if entries is not None:

            self.entries = entries
            self.rowcount = len(entries)
            self.columncount = len(entries[0])

        elif rowcount > 0 and columncount > 0:

            self.rowcount = rowcount
            self.columncount = columncount

            self.entries = []
            for row in range(0, self.rowcount):
                self.entries.append([0] * self.columncount)

    def __str__(self):

        """
        Returns the matrix formatted with square brackets
        and rows on separate lines.
        """

        brackets = {"top_left": "\u23A1",
                    "middle_left": "\u23A2",
                    "bottom_left": "\u23A3",
                    "top_right": "\u23A4",
                    "middle_right": "\u23A5",
                    "bottom_right": "\u23A6"}

        string = []

        for index, row in enumerate(self.entries):

            if index == 0:
                string.append(brackets["top_left"])
            elif index == self.rowcount - 1:
                string.append(brackets["bottom_left"])
            else:
                string.append(brackets["middle_left"])

            for column in row:
                string.append("{:4}".format(column))

            if index == 0:
                string.append(brackets["top_right"])
            elif index == self.rowcount - 1:
                string.append(brackets["bottom_right"])
            else:
                string.append(brackets["middle_right"])

            string.append("\n")

        return "".join(string)

    def __add__(self, other):

        """
        Matrix addition returns a matrix the same shape as the two being added
        with each value the sum of the corresponding values.
        """

        if self.addable(other):

            result = Matrix(rowcount=self.rowcount, columncount=self.columncount)

            for row in range(0, self.rowcount):
                for column in range(0, self.columncount):
                    result.entries[row][column] = self.entries[row][column] + other.entries[row][column]

            return result

        else:

            raise ValueError("Matrices must have the same shape to be added")

    def __sub__(self, other):

        """
        Matrix subtraction returns a matrix the same shape as the two being added
        with each value being the first value minus its corresponding second value.
        """

        if self.subtractable(other):

            result = Matrix(rowcount=self.rowcount, columncount=self.columncount)

            for row in range(0, self.rowcount):
                for column in range(0, self.columncount):
                    result.entries[row][column] = self.entries[row][column] - other.entries[row][column]

            return result

        else:

            raise ValueError("Matrices must have the same shape to be subtracted")

    def __mul__(self, scalar):

        """
        Scalar multiplication returns a matrix the same shape as the original,
        each value being multiplied by the scalar.
        """

        result = Matrix(rowcount=self.rowcount, columncount=self.columncount)

        for row in range(0, self.rowcount):
            for column in range(0, self.columncount):
                result.entries[row][column] = self.entries[row][column] * scalar

        return result

    def __matmul__(self, other):

        """
        The result of matrix multiplication is a matrix with the same number
        of rows as the first matrix and the same number of columns as the second.
        Each value is the dot product of the corresponding row and column.
        """

        if self.multipliable(other):

            result = Matrix(rowcount=self.rowcount, columncount=other.columncount)

            for row in range(0, result.rowcount):
                for column in range(result.columncount):
                    result.entries[row][column] = self.__dot_product(other, row, column)

            return result

        else:

            raise ValueError("Matrices not of the right shapes to be multiplied")

    def addable(self, other):

        """
        To be addable matrices must each have the same number of rows and columns.
        """

        return self.rowcount == other.rowcount and self.columncount == other.columncount

    def subtractable(self, other):

        """
        To be subtractable matrices must each have the same number of rows and columns.
        """

        return self.rowcount == other.rowcount and self.columncount == other.columncount

    def multipliable(self, other):

        """
        To be multipliable the number of rows in the second matrix must
        be the same as the number of columns in the first matrix.
        """

        return self.columncount == other.rowcount

    def __dot_product(self, other, self_row, other_column):

        """
        Calculate the sum of the products of the corresponding values
        in the specified row and column.
        """

        dot_product = 0

        for i in range(0, self.columncount):

            dot_product += (self.entries[self_row][i] * other.entries[i][other_column])

        return dot_product
