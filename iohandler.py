import sys

#
# each of the past day's weather will be stored on an individual line from one day to the next
#  line 1 = day 1, line 2 = day 2 and so on
#  Only the 8 most recent lines will be kept in the data file.
#  Assuming that the update command is automated and run once a day at the same time every day.
#   Dates are stored in European Fashion
#

class IOHandler:

    def __init__(self, date):
        self.file_name = ''
        self.temperatures = []
        self.current_date = date
        #print(self.current_date)

    def get_most_recent_entry(self):
        with open('data') as file:
            most_recent_entry = file.readline()
        most_recent_date = most_recent_entry.split()[1]
        return most_recent_date

    def get_weather(self, day):

        with open('data') as file:
            # get temperatures
            self.temperatures = file.readlines()

            # error checking for data
            if len(self.temperatures) < day:
                print('ERROR: NO DATA FOR GIVEN DAY')
                sys.exit(-3)

        # retun temperatue of the given day
        temp = self.temperatures[day].split()[0]
        return int(temp)

    def update_weather(self, today):

        # read existing lines and close file
        with open('data', 'r') as file:
            lines = file.readlines()

        with open('data', 'w') as file:
            file.writelines([str(today) + ' ' +  self.current_date + '\n', ] + lines[:8])
            #print(lines)


