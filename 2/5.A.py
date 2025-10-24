print("This program calculates times table")
tablenum = input("\nWhich multiplication table shall I generate for you? ")
tablenum = int(tablenum)
print("\nHere is your", tablenum, "times table:\n")
for i in range(1, 13 + 1):
    value = int(i * tablenum)
    if value % 2 != 0:
        print(i, "times", tablenum, "is", value)
        print("------------------")
