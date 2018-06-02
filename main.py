import sys
import api, logic, iohandler

# initialize different components of the script
yandex_api = api()

def main():

    #string for the output
    output = " "

    # update data
    if sys.argv(2) == 'update':
        yandex_api.update()
    # otherwise check the difference between the current day and the requested day
    else:
        # error checking
        if not len(sys.argv) == 2:
            print("Invalid Number of Arguments: " + str(len(sys.argv)) + " Please Specify Only 2")
            sys.exit(-1)

        elif (sys.argv(2) < 1 or sys.argv(2) > 7):
            print("Invalid Argument: " + str(sys.argv(2)) + "Argument must be between 1 and 7 days")
            sys.exit(-2)

        # find difference
        else:
            day = sys.argv(2)
            output = "Сегоднящная погода отличается от предсказанной " + str(day) + " день/дня/дней назад на "\
                     + str(logic.find_difference(day)) + "%"


            print(output)


    sys.exit(0)