import datetime
from datetime import date
def main():

    #firstDate = datetime.date(1901, 1, 1)
    #lastDate = datetime.date(2000, 12, 31)
    #date=lastDate-firstDate
    #print(date)
    x = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if (date(y, m, 1).weekday()==6):
                x += 1

    print(x)





if __name__ == '__main__':
    main()