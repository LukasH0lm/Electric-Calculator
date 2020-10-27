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
    known = int(input("choose:"))
    if known == 1:
        V = int(input("Enter V: "))
        R = int(input("Enter R: "))
        print(V ** 2 / R)
    if known == 2:
        R = int(input("Enter R: "))
        A = int(input("Enter A: "))
        print(R * A ** 2)
    if known == 3:
        A = int(input("Enter A: "))
        V = int(input("Enter V: "))
        print(V * A)


def find_v():
    print("please choose a set of known variables:")
    print("1: R and A")
    print("2: A and W")
    print("3: W and R")
    known = int(input("choose:"))
    if known == 1:
        R = int(input("Enter R: "))
        A = int(input("Enter A: "))
        print(R * A)
    if known == 2:
        A = int(input("Enter A: "))
        W = int(input("Enter W: "))
        print(W / A)
    if known == 3:
        W = int(input("Enter W: "))
        R = int(input("Enter R: "))
        print(math.sqrt(W * R))


def find_a():
    print("please choose a set of known variables:")
    print("1: W and R")
    print("2: W and V")
    print("3: V and R")
    known = int(input("choose:"))
    if known == 1:
        W = int(input("Enter W: "))
        R = int(input("Enter R: "))
        print(math.sqrt(W/R))
    if known == 2:
        W = int(input("Enter W: "))
        V = int(input("Enter V: "))
        print(W / V)
    if known == 3:
        V = int(input("Enter V: "))
        R = int(input("Enter R: "))
        print(V / R)


def find_r():
    print("please choose a set of known variables:")
    print("1: V and A")
    print("2: A and V")
    print("3: W and A")
    known = int(input("choose:"))
    if known == 1:
        V = int(input("Enter V: "))
        A = int(input("Enter A: "))
        print(V / A)
    if known == 2:
        A = int(input("Enter A: "))
        V = int(input("Enter V: "))
        print(V ** 2 / A)
    if known == 3:
        W = int(input("Enter W: "))
        A = int(input("Enter A: "))
        print(W / A ** 2)


if __name__ == "__main__":
    main()
#test