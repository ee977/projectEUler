def main():
    theOne = 1
    time = 0
    while(time <= 999):
        theOne *=2
        time+=1

    sum = 0
    for digit in str(theOne):
      sum += int(digit)

    print(sum)



if __name__ == '__main__':
    main()
