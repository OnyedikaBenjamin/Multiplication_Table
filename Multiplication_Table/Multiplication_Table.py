print("                    Multiplication Table")
print("        ", end="")
for i in range(1, 10):
    print(i, end="     ")
print()
print("-------------------------------------------------------------")
print()
for j in range(1, 10):
    print(j, "|", end="")
    for k in range(1, 10):
        if j * k > 9:
            print("   ", j * k, end="")
        else:
            print("    ", j * k, end="")
    print()
