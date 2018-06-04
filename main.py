import sys
import api, iohandler

# initialize different components of the script globally
filehandler = iohandler.IOhandler()
yandex_api = api.Api(filehandler)


# get the difference between today and the given day
def find_difference(day):

    # get figures for comparison
    today = 20#yandex_api.get_weather()
    other = 21 #filehandler.get_weather(day)

    #find the percentage difference between the days
    difference = ((today - other) /((today + other) / 2)) * 100

    return difference

# update the data in the data textfile
def update():
    print('update')
    today = yandex_api.get_weather()
    filehandler.update_weather(today)

# find the difference between today and the given day
def find(day):
    print('find')
    if (day < 1 or day > 7):
        print("Invalid Argument to FIND: " + str(day) + " Argument must be between 1 and 7 days")
        sys.exit(-2)

    output = "Сегоднящная погода отличается от предсказанной " + str(day) + " день/дня/дней назад на " \
             + str(find_difference(day)) + "%"

    return output

def main():

    print('hello')
    # update data
    if sys.argv[1] == 'update':
        update()
    # otherwise check the difference between the current day and the requested day

        # find difference
    elif sys.argv[1] == 'find':
        # error checking
        if not len(sys.argv) == 3:
            print("Invalid Number of Arguments: " + str(len(sys.argv)) + " Please Specify Day")
            sys.exit(-1)

        # print results
        print(
            find(int(sys.argv[2])))

    else:
        print("Invalid Command: Only update and find accepted")
        sys.exit(-1)
    # exit script
    sys.exit(0)

if __name__ == '__main__':
    main()