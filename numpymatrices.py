import numpy


def main():

    print("------------------")
    print("| codedrome.com  |")
    print("| NumPy Matrices |")
    print("------------------\n")

    m1 = numpy.array([[1,2,3],[4,5,6]])
    m2 = numpy.array([[7,10],[8,11],[9,12]])
    m3 = numpy.array([[9,8,7],[6,5,4]])

    print("m1\n=========\n{}".format(m1))
    print()
    print("m2\n=========\n{}".format(m2))
    print()
    print("m3\n=========\n{}".format(m3))
    print()

    added = m1 + m3
    print("m1 + m3\n============\n{}".format(added))
    print()

    addedscalar = m1 + 7
    print("m1 + 7\n============\n{}".format(addedscalar))
    print()

    multipliedscalar = m1 * 3
    print("m1 * 3\n============\n{}".format(multipliedscalar))
    print()

    multiplied = m1 @ m2
    print("m1 @ m2\n===========\n{}".format(multiplied))
    print()


main()
