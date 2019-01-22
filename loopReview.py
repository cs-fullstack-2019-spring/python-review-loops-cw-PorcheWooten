def main():
    # # exercise1()
    # exercise2()
    exercise3()


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# # Hint: Use 'continue' statement.
# # Expected Output : 0 1 2 4 5

def exercise1():
    for n in range(0, 6):
        if n == 3:
            continue
        print(n)


# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def exercise2():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    evenCount = 0
    oddCount = 0
    for n in numbers:
        if (n % 2 == 0):
            evenCount = evenCount +1
        else:
            oddCount = oddCount +1
    print("Number of even number: ", evenCount)
    print("Number of odd numbers: ", oddCount)


#Write a Python program that accepts a sequence of lines (blank line to terminate) as input
#and prints the lines as output after User enters a blank line to end.
#Do not use an array to hold the lines of text
def exercise3():
    allInput = ""

    while (True):
        userInput =input("Enter something ")
        if userInput == "":
            break

        allInput += (userInput + "\n")

    print(allInput)


if __name__ == '__main__':
    main()
