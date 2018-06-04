import sys

class IOhandler:

    def __init__(self):
        self.filename = ''
        self.temperatures = []

# each of the past day's weather will be stored on an individual line from one day to the next
    #  line 1 = day 1, line 2 = day 2 and so on
    def get_weather(self, day):

        file = open('data', 'r')
        # get temperatures
        self.temperatures = file.readlines()

        # error checking for data
        if len(self.temperatures) < day:
            print('ERROR: NO DATA FOR GIVEN DAY')
            sys.exit(-3)

        file.close()

        # retun temperatue of the given day
        print(self.temperatures)
        return int(self.temperatures[day])

    def update_weather(self, today):

        # read existing lines and close file
        file = open('data', 'r')
        lines = file.readlines()
        print(lines)
        file.close()

        # open file for writing and erase old data
        file = open('data', 'w')
        print(lines)
        file.writelines([str(today) + '\n'] + lines[:7])
        file.close()
        file = open('data', 'r')
        new_lines = file.readlines()
        print(new_lines)



