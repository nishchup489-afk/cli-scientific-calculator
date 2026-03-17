import math

print("""
1) Arithmetic
2) Trigonometric
3) Logarithms
4) Powers and Roots
5) Factorials
6) Constants (pi and e)
""")

choice = int(input("Enter your choice (1-6): "))


def arithmetic():
    expr = input("Enter expression (example: 5+3*2): ")
    result = eval(expr)
    print("Result:", result)


def trigonometric():
    print("""
1) sin
2) cos
3) tan
""")

    op = int(input("Choose operation: "))
    angle = float(input("Enter angle in degrees: "))

    rad = math.radians(angle)

    if op == 1:
        print("Result:", math.sin(rad))
    elif op == 2:
        print("Result:", math.cos(rad))
    elif op == 3:
        print("Result:", math.tan(rad))


def logarithm():
    num = float(input("Enter number: "))

    print("""
1) log10
2) ln
""")

    op = int(input("Choose: "))

    if op == 1:
        print("Result:", math.log10(num))
    elif op == 2:
        print("Result:", math.log(num))


def powers_roots():
    print("""
1) Power
2) Square Root
""")

    op = int(input("Choose: "))

    if op == 1:
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result:", math.pow(a, b))

    elif op == 2:
        x = float(input("Enter number: "))
        print("Result:", math.sqrt(x))


def factorial():
    n = int(input("Enter number: "))
    print("Result:", math.factorial(n))


def constants():
    print("pi =", math.pi)
    print("e =", math.e)


if choice == 1:
    arithmetic()

elif choice == 2:
    trigonometric()

elif choice == 3:
    logarithm()

elif choice == 4:
    powers_roots()

elif choice == 5:
    factorial()

elif choice == 6:
    constants()

else:
    print("Invalid choice")