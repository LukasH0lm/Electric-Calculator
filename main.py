import math

def main():
    goal = input("Please enter what you find to find: ")
    if goal == "W":
        find_w()
    elif goal == "V":
        find_v()
    elif goal == "A":
        find_a()
    elif goal == "R":
        find_r()

def find_w():
    print("please choose a set of known variables:")
    print("1: V and R")
    print("2: R and A")
    print("3: A and V")
    known = float(input("choose:"))
    if known == 1:
        V = float(input("Enter V: "))
        R = float(input("Enter R: "))
        print("\nusing the formula P = U^2 / Ohm")
        print("\nW = ")
        print(V ** 2 / R)
    if known == 2:
        R = float(input("Enter R: "))
        A = float(input("Enter A: "))
        print("\nusing the formula P = Ohm * I^2")
        print("\nW = ")
        print(R * A ** 2)
    if known == 3:
        A = float(input("Enter A: "))
        V = float(input("Enter V: "))
        print("\nusing the formula P = U * I")
        print("\nW = ")
        print(V * A)


def find_v():
    print("please choose a set of known variables:")
    print("1: R and A")
    print("2: A and W")
    print("3: W and R")
    known = float(input("choose:"))
    if known == 1:
        R = float(input("Enter R: "))
        A = float(input("Enter A: "))
        print("\nusing the formula U = Ohm * I")
        print("\nV = ")
        print(R * A)
    if known == 2:
        A = float(input("Enter A: "))
        W = float(input("Enter W: "))
        print("\nusing the formula U = P / I")
        print("\nV = ")
        print(W / A)
    if known == 3:
        W = float(input("Enter W: "))
        R = float(input("Enter R: "))
        print("\nusing the formula U = sqrt(P * Ohm)")
        print("\nV = ")
        print(math.sqrt(W * R))


def find_a():
    print("please choose a set of known variables:")
    print("1: W and R")
    print("2: W and V")
    print("3: V and R")
    known = float(input("choose:"))
    if known == 1:
        W = float(input("Enter W: "))
        R = float(input("Enter R: "))
        print("\nusing the formula I = sqrt(P / Ohm) ")
        print("\nA = ")
        print(math.sqrt(W/R))
    if known == 2:
        W = float(input("Enter W: "))
        V = float(input("Enter V: "))
        print("\nusing the formula I = P / U")
        print("\nA = ")
        print(W / V)
    if known == 3:
        V = float(input("Enter V: "))
        R = float(input("Enter R: "))
        print("\nusing the formula I = U / Ohm")
        print("\nA = ")
        print(V / R)


def find_r():
    print("please choose a set of known variables:")
    print("1: V and A")
    print("2: V and W")
    print("3: W and A")
    known = float(input("choose:"))
    if known == 1:
        V = float(input("Enter V: "))
        A = float(input("Enter A: "))
        print("\nusing the formula Ohm = U / I")
        print("\nR = ")
        print(V / A)
    if known == 2:
        A = float(input("Enter A: "))
        W = float(input("Enter W: "))
        print("\nusing the formula Ohm = U^2 / P")
        print("\nR = ")
        print(W ** 2 / A)
    if known == 3:
        W = float(input("Enter W: "))
        A = float(input("Enter A: "))
        print("\nusing the formula Ohm = P / I^2")
        print("\nR = ")
        print(W / A ** 2)


if __name__ == "__main__":
    main()
#test