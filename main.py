import sys
import parser, iohandler
import datetime

# weather page url
url = 'https://yandex.ru/pogoda/moscow'
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# initialize different components of the script globally
file_handler = iohandler.IOHandler(current_date)
yandex_scraper = parser.YandexParser(url)


# get the difference between today and the given day
# Integer (# of days ago) --> Integer (% difference)
def find_difference(day):

    # get figures for comparison
    # check data first, if not updated go to yandex
    if file_handler.get_most_recent_entry() == current_date:
        today = file_handler.get_weather(0)
    else:
        today = yandex_scraper.get_weather()
        # update data too
        file_handler.update_weather(today)

    other = file_handler.get_weather(day)

    #find the percentage difference between the days
    print(str(today))
    print(str(other))
    difference = ((today - other) /((today + other) / 2)) * 100

    return difference

# Get current weather from yandex webpage. Write that weather into the data file.
# will only update if it wasn't updated today
# ~ -> ~
def update():
    if not file_handler.get_most_recent_entry() == current_date:
        today = yandex_scraper.get_weather()
        file_handler.update_weather(today)

# find the difference between today and the given day
# Integer (# of days ago) --> String (Target String for displaying difference)
def find(day):
    print('find')
    if (day < 1 or day > 7):
        print("Invalid Argument to FIND: " + str(day) + " Argument must be between 1 and 7 days")
        sys.exit(-2)

    output = "Сегоднящная погода отличается от предсказанной " + str(day) + " день/дня/дней назад на " \
             + str(find_difference(day)) + "%"

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
        print(find(int(sys.argv[2])))

    else:
        # invalid command line arguments
        print("Invalid Command: Only update and find commands accepted")
        sys.exit(-1)
    # exit script
    sys.exit(0)

if __name__ == '__main__':
    main()