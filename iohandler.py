import sys
import datetime

#
# each of the past day's weather will be stored on an individual line from one day to the next
#  line 1 = day 1, line 2 = day 2 and so on
#  Only the 8 most recent lines will be kept in the data file.
#  Assuming that the update command is automated and run once a day at the same time every day.
#
#

class IOhandler:

    def __init__(self):
        self.filename = ''
        self.temperatures = []


    def get_weather(self, day):

        with open('data') as file:
            # get temperatures
            self.temperatures = file.readlines()

            # error checking for data
            if len(self.temperatures) < day:
                print('ERROR: NO DATA FOR GIVEN DAY')
                sys.exit(-3)

        # retun temperatue of the given day
        return int(self.temperatures[day])

    def update_weather(self, today):

        # read existing lines and close file
        with open('data', 'r') as file:
            lines = file.readlines()

        # open file for writing and erase old data
        with open('data', 'w') as file:
            file.writelines([str(today) + '\n', ] + lines[:7])
            print(lines)


