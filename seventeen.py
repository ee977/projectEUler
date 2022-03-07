def main():
    max = 1
    letter = 0
    while max <= 1000:
        string=str(max)
        #print(range(len(string)))

        for i in range(len(string)):

            #print(len(string)-i-1)


            if len(string)-i-1 == 0:
                if '1' == string[i]:  # ONE
                    letter += 3
                elif '2' == string[i]:  # TWO
                    letter += 3
                elif '3' == string[i]:  # THREE
                    letter += 5
                elif '4' == string[i]:  # FOUR
                    letter += 4
                elif '5' == string[i]:  # FIVE
                    letter += 4
                elif '6' == string[i]:  # SIX
                    letter += 3
                elif '7' == string[i]:  # SEVEN
                    letter += 5
                elif '8' == string[i]:  # EIGHT
                    letter += 5
                elif '9' == string[i]:  # NINE
                    letter += 4
            elif len(string)-i-1 == 1:
                if '1' == string[i]:  # with ten
                    if '1' == string[i+1]:  # eleven
                        letter += 6-3
                    elif '2' == string[i+1]:  # twelve
                        letter += 6-3
                    elif '3' == string[i+1]:  # thirteen
                        letter += 8-5
                    elif '4' == string[i+1]:  # fourteen
                        letter += 8-4
                    elif '5' == string[i+1]:  # fifteen
                        letter += 7-4
                    elif '6' == string[i+1]:  # sixteen
                        letter += 7-3
                    elif '7' == string[i+1]:  # seventeen
                        letter += 9-5
                    elif '8' == string[i+1]:  # eighteen
                        letter += 8-5
                    elif '9' == string[i+1]:  # nineteen
                        letter += 8-4
                    elif '0' == string[i+1]:  # for ten only!!!!!!!!!!!!!!!
                        letter += 3
                elif '2' == string[i]:  # twenty
                    letter += 6
                elif '3' == string[i]:  # thirty
                    letter += 6
                elif '4' == string[i]:  # forty
                    letter += 5
                elif '5' == string[i]:  # fifty
                    letter += 5
                elif '6' == string[i]:  # sixty
                    letter += 5
                elif '7' == string[i]:  # seventy
                    letter += 7
                elif '8' == string[i]:  # eighty
                    letter += 6
                elif '9' == string[i]:  # ninety
                    letter += 6

            elif len(string)-i-1 == 2:
                if '1' == string[i]:  # ONE hundred and
                    letter += 3 + 10
                elif '2' == string[i]:  # TWO hundred and
                    letter += 3 + 10
                elif '3' == string[i]:  # THREE hundred and
                    letter += 5 + 10
                elif '4' == string[i]:  # FOUR hundred and
                    letter += 4 + 10
                elif '5' == string[i]:  # FIVE hundred and
                    letter += 4 + 10
                elif '6' == string[i]:  # SIX hundred and
                    letter += 3 + 10
                elif '7' == string[i]:  # SEVEN hundred and
                    letter += 5 + 10
                elif '8' == string[i]:  # EIGHT hundred and
                    letter += 5 + 10
                elif '9' == string[i]:  # NINE hundred and
                    letter += 4 + 10




            elif len(string)-i-1 == 3:
                #if '1' == string[i]:   # one thousand
                letter += 3+8



        max += 1
    # there are extra 'and's which i just substract from the total amount such as 100, 200, 300, ... they have addional 'and's
    letter-(3*9)
    print(letter)


if __name__ == '__main__':
    main()