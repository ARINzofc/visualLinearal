import math
import numpy as a

from operations import (
    vector_addition, vector_subtract, vector_multiple,
    vector_mag, vector_dot, matrix_tranform, square,
    unit_vector, projection, linear_combination, linear_independece
)
from visualizer import (
    vector_draw, matrix_draw, eignvector,
    vector_draw2, vector_draw3, vector_draw4, vector_draw5
)
def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



def intro():
    A = get_number("Enter i component of A: ")
    A2 = get_number("Enter j component of A: ")
    B = get_number("Enter i component of B: ")
    B2 = get_number("Enter j component of B: ")
    n = a.array([A, A2])
    p = a.array([B, B2])
    return n, p
    
def introm():
    A = get_number("Enter row 1, column 1: ")
    A2 = get_number("Enter row 1, column 2: ")
    B = get_number("Enter row 2, column 1: ")
    B2 = get_number("Enter row 2, column 2: ")
    v1 = get_number("Enter the vector x: ")
    v2 = get_number("Enter the vector y: ")
    c = a.array([v1, v2])
    n = a.array([[A, A2], [B, B2]])
    return n, c


def introT():

    a1 = get_number("Enter row 1, column 1: ")
    b1 = get_number("Enter row 1, column 2: ")
    c1 = get_number("Enter row 2, column 1: ")
    d1 = get_number("Enter row 2, column 2: ")

    a2 = get_number("Enter row 1, column 1 of second matrix: ")
    b2 = get_number("Enter row 1, column 2 of second matrix: ")
    c2 = get_number("Enter row 2, column 1 of second matrix: ")
    d2 = get_number("Enter row 2, column 2 of second matrix: ")

    matrix1 = a.array([
        [a1, b1],
        [c1, d1]
    ])

    matrix2 = a.array([
        [a2, b2],
        [c2, d2]
    ])

    return matrix1, matrix2

print("""
╔══════════════════════════════════════╗
║      NUMPY LINEAR ALGEBRA            ║
║           VISUALIZER                 ║
╚══════════════════════════════════════╝
""")

print("1. Vector Operations")
print("2. Matrix Operations")
print("3. Vector Spaces")
print("4. Transformations")
print("5. Orthogonality")
print("6. Eigenvalues & Eigenvectors")
print("7. Exit")

Enter = get_number("Enter your choice: ")

if Enter == 1:

    print("Vector Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Element-wise Multiplication")
    print("4. Magnitude")
    print("5. Dot Product")
    print("6. Unit Vector")
    print("7. Projection")
    print("8. Linear Combination")
    print("9. Linear Independence")

    Enter3 = get_number("Enter the choice: ")

    if Enter3 == 1:
        n, p = intro()
        result = vector_addition(n, p)
        print("Addition:", result)
        vector_draw(n, p, result)

    elif Enter3 == 2:
        n, p = intro()
        result = vector_subtract(n, p)
        print("Subtraction:", result)
        vector_draw2(n, p, result)

    elif Enter3 == 3:
        n, p = intro()
        result = vector_multiple(n, p)
        print("Element-wise Multiplication:", result)
        vector_draw3(n, p, result)

    elif Enter3 == 4:
        n, p = intro()
        print("Magnitude of A:", vector_mag(n))
        print("Magnitude of B:", vector_mag(p))

    elif Enter3 == 5:
        n, p = intro()
        result = vector_dot(n, p)
        print("Dot product:", result)
        vector_draw4(n, p, result)

    elif Enter3 == 6:
        n, p = intro()
        print("Unit vector of A:", unit_vector(n))
        print("Unit vector of B:", unit_vector(p))

    elif Enter3 == 7:
        n, p = intro()
        result = projection(n, p)
        print("Projection:", result)
        vector_draw5(n, p, result)

    elif Enter3 == 8:
        n, p = intro()
        b = get_number("Coefficient of A: ")
        c = get_number("Coefficient of B: ")
        print(
            "Linear Combination:",
            linear_combination(n, p, b, c)
        )
    elif Enter3 == 9:
        n, p = intro()
        print(linear_independece(n, p))

    else:
        print("Invalid choice.")

elif Enter == 2:

    print("Matrix Operations")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")

    choice = get_number("Enter your choice: ")

    matrix1, matrix2 = introT()

    if choice == 1:
        print("Addition:", matrix1 + matrix2)

    elif choice == 2:
        print("Subtraction:", matrix1 - matrix2)

    elif choice == 3:
        print("Multiplication:", a.matmul(matrix1, matrix2))

    elif choice == 4:
        print("Transpose:", matrix1.T)

    elif choice == 5:
        print("Determinant:", a.linalg.det(matrix1))

    elif choice == 6:
        print("Inverse:", a.linalg.inv(matrix1))

    else:
        print("Invalid choice.")

elif Enter == 3:

    print("Vector Spaces")
    print("""
1. Linear Combination
2. Vector Space Check
3. Basis
4. Dimension
""")

    enter4 = get_number("Enter your choice: ")

    if enter4 == 1:

        print("Linear Combination")

        n, p = intro()

        c1 = get_number("Enter coefficient for A: ")
        c2 = get_number("Enter coefficient for B: ")

        print(
            "Linear Combination:",
            linear_combination(n, p, c1, c2)
        )

    elif enter4 == 2:

        print("Vector Space Checks")

        n, p = intro()
        E = get_number("Enter the scalar: ")

        result = vector_addition(n, p)
        mult = E * n

        print("Addition:", result)

        if result.shape[0] == 2 and mult.shape[0] == 2:
            print("Both remain in R^2")
        else:
            print("They are not both in R^2")

    elif enter4 == 3:

        print("Basis")

        n, p = intro()
        c = a.array([n, p])

        if a.linalg.det(c) == 0:
            print("Vectors are dependent and cannot form a basis")
        else:
            print("Vectors are independent and can form a basis")

    elif enter4 == 4:

        print("Dimension")

        n, p = intro()

        c = a.array([n, p])
        d = a.linalg.matrix_rank(c)

        print("Dimension:", d)

    else:
        print("Invalid choice.")

elif Enter == 4:

    print("Linear Transformation")
    print("1. Scaling")
    print("2. Rotation")
    print("3. Shear")
    print("4. Custom Matrix Transformation")

    Enter5 = get_number("Enter the choice: ")

    if Enter5 == 1:

        print("Scaling")

        v1 = get_number("Enter vector x: ")
        v2 = get_number("Enter vector y: ")
        v4 = get_number("Enter scaling factor: ")

        v3 = a.array([v1, v2])
        multi = v4 * v3

        print("Original Vector:", v3)
        print("Scaled Vector:", multi)

        matrix_draw(v3, multi)


    elif Enter5 == 2:

        print("Rotation")

        r1 = get_number("Enter vector x: ")
        r2 = get_number("Enter vector y: ")

        ra = a.array([r1, r2])

        deg = get_number("Enter rotation angle: ")

        rad = math.radians(deg)

        rota = a.array([
            [a.cos(rad), a.sin(rad)],
            [-a.sin(rad), a.cos(rad)]
        ])

        mul = matrix_tranform(ra, rota)

        print("Original vector:", ra)
        print("Rotated vector:", mul)

        matrix_draw(ra, mul)


    elif Enter5 == 3:

        print("Shear")
        print("1. X-Shear")
        print("2. Y-Shear")

        choose = get_number("Enter the choice: ")

        if choose == 1:

            sx = get_number("Enter x vector: ")
            sy = get_number("Enter y vector: ")
            k = get_number("Enter shear factor: ")

            sm = a.array([sx, sy])

            sl = a.array([
                [1, k],
                [0, 1]
            ])

            trans = a.matmul(sl, sm)

            print("X-Shear:", trans)

            matrix_draw(sm, trans)


        elif choose == 2:

            sx = get_number("Enter x vector: ")
            sy = get_number("Enter y vector: ")
            k = get_number("Enter shear factor: ")

            sm = a.array([sx, sy])

            sl = a.array([
                [1, 0],
                [k, 1]
            ])

            trans = a.matmul(sl, sm)

            print("Y-Shear:", trans)

            matrix_draw(sm, trans)

        else:
            print("Invalid shear choice.")


    elif Enter5 == 4:

        n, c = introm()

        mul = matrix_tranform(n, c)

        print("Original matrix:", n)
        print("Transformed vector:", mul)

        matrix_draw(c, mul)

    else:
        print("Invalid choice.")

elif Enter == 5:

    print("Orthogonality")

    n, p = intro()

    dot = a.dot(n, p)

    print("Dot Product:", dot)

    if a.isclose(dot, 0):
        print("Yes → Orthogonal")
    else:
        print("No → Not Orthogonal")

elif Enter == 6:

    print("Eigenvalues & Eigenvectors")

    A = get_number("Enter row 1, column 1: ")
    A2 = get_number("Enter row 1, column 2: ")
    B = get_number("Enter row 2, column 1: ")
    B2 = get_number("Enter row 2, column 2: ")

    n = a.array([
        [A, A2],
        [B, B2]
    ])

    c = a.linalg.eig(n)

    print("Eigenvalues:", c[0])
    print("Eigenvectors:", c[1])

    if a.iscomplexobj(c[1]):
        print(
            "Eigenvectors are complex and cannot be "
            "visualized on a normal real 2D graph."
        )
    else:
        eignvector(c[1])

elif Enter == 7:

    print("Thank you for using the Linear Algebra Visualizer.")

else:

    print("Invalid main menu choice.")
