def main():
    n = 100
    total = 1
    top = 0

    for x in range(1, n+1):
        total *= x
    print(total)
    string = str(total)
    for i in range(len(string)):

        top += int(string[i])

    print(top)


if __name__ == '__main__':

    main()
