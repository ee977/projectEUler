# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.

def main():
        triangleNumber = 0
        factor = 0
        number = 1
        y = 1
        n = 1
        max = 501         #give max plus 1 of the number needed
        while (factor < max):
            factor = 0
            y = number
            triangleNumber = 0

            while (y != 0):
                triangleNumber += y
                y -= 1

            n = 1

            i = 1
            k = int(triangleNumber ** 0.5)
            while (i <= k and factor != max):
                if (triangleNumber % i == 0):
                    factor += 2
                    if (i * i == triangleNumber):
                        factor -= 1
                    #             print(str(factor))
                #            print(str(factor))

                i += 1

            number += 1

        print("Number: " + str((number - 1)))
        print("Triangle number: " + str(triangleNumber))
        print("Factor count: " + str(factor))


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
