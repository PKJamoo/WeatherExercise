import sys
import parser, iohandler

# weather page url
url = 'https://yandex.ru/pogoda/moscow'

# initialize different components of the script globally
filehandler = iohandler.IOhandler()
yandex_scraper = parser.Yandex_Parser(url)


# get the difference between today and the given day
# Integer (# of days ago) --> Integer (% difference)
def find_difference(day):

    # get figures for comparison
    today = yandex_scraper.get_weather()
    other = filehandler.get_weather(day)

    #find the percentage difference between the days
    print(str(today))
    print(str(other))
    difference = ((today - other) /((today + other) / 2)) * 100

    return difference

# Get current weather from yandex webpage. Write that weather into the data file.
# ~ -> ~
def update():
    today = yandex_scraper.get_weather()
    filehandler.update_weather(today)

# find the difference between today and the given day
# Integer (# of days ago) --> String (Target String for displaying difference)
def find(day):
    print('find')
    if (day < 1 or day > 7):
        print("Invalid Argument to FIND: " + str(day) + " Argument must be between 1 and 7 days")
        sys.exit(-2)

    output = "Сегоднящная погода отличается от предсказанной " + str(day) + " день/дня/дней назад на " \
             + str(find_difference(day - 1)) + "%"

    return output

def main():

    # update data command
    if sys.argv[1] == 'update':
        update()
    # find difference command
    elif sys.argv[1] == 'find':
        # invalid number of arguments
        if not len(sys.argv) == 3:
            print("Invalid Number of Arguments: " + str(len(sys.argv)) + " Please Specify Day")
            sys.exit(-1)

        # print results
        print(
            find(int(sys.argv[2])))

    else:
        # invalid command line arguments
        print("Invalid Command: Only update and find commands accepted")
        sys.exit(-1)
    # exit script
    sys.exit(0)

if __name__ == '__main__':
    main()