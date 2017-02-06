# One small error.  Your grids run together.  You left an open end= " " print without a return.

def print_grid(n):
    for j in range(2):
        print("+" + ((" -" * int(n / 2)) + " +") * 2, end=" ")
        print()
        for i in range(int(n/2)):
            print("|" + ("  " * int(n/2)) + " |" + ("  " * int(n/2)) + " |", end = " ")
            print()
    print("+" + ((" -" * int(n / 2)) + " +") * 2, end=" ")

print_grid(3)


def print_grid2(n, m):
    for j in range(n):
        print("+" + ((" -" * int(m)) + " +")*n, end = " ")
        print()
        for i in range(int(m)):
            print("|" + (("  " * int(m)) + " |")*n, end = " ")
            print()
    print("+" + ((" -" * int(m)) + " +") * n, end=" ")
    print()
print_grid2(5, 3)
print_grid2(3,3)
