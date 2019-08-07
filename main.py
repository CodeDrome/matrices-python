import matrix


def main():

    print("----------------------")
    print("| codedrome.com      |")
    print("| Exploring Matrices |")
    print("----------------------\n")

    addition()

    #subtraction()

    #scalar_multiplication()

    # matrix_multiplication()


def addition():

    print("Addition\n--------")

    m1 = matrix.Matrix(entries=[[1,2,3],[4,5,6]])
    m2 = matrix.Matrix(entries=[[2,3,4],[3,4,5]])
    m3 = matrix.Matrix(entries=[[2,3],[3,4,5]])

    print("m1 and m2 addable? {}".format(m1.addable(m2)))
    print("m1 and m3 addable? {}\n".format(m1.addable(m3)))

    m1_plus_m2 = m1 + m2

    print(m1)
    print(m2)
    print(m1_plus_m2)


def subtraction():

    print("Subtraction\n-----------")

    m4 = matrix.Matrix(entries=[[9,8,7],[8,7,6]])
    m5 = matrix.Matrix(entries=[[1,2,3],[3,4,5]])
    m6 = matrix.Matrix(entries=[[8,7],[6,5,4]])

    print("m4 and m5 subtractable? {}".format(m4.subtractable(m5)))
    print("m4 and m6 subtractable? {}".format(m4.subtractable(m6)))

    m4_minus_m5 = m4 - m5

    print(m4)
    print(m5)
    print(m4_minus_m5)


def scalar_multiplication():

    print("Scalar multiplication\n---------------------")

    m7 = matrix.Matrix(entries=[[2,4,6],[8,10,12]])

    m8 = m7 * 3

    print(m7)
    print(m8)


def matrix_multiplication():

    print("Matrix multiplication\n---------------------")

    m9 = matrix.Matrix(entries=[[1,2,3],[4,5,6]])
    m10 = matrix.Matrix(entries=[[7,10],[8,11],[9,12]])

    print("m9 and m10 multipliable? {}".format(m9.multipliable(m10)))

    print(m9)
    print(m10)

    m9_x_m10 = m9 @ m10

    print(m9_x_m10)


main()
