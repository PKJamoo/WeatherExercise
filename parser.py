import urllib.request
from html.parser import HTMLParser


class Yandex_Parser(HTMLParser):


    def __init__(self, IOhandler, url):
        # call to super
        HTMLParser.__init__(self)
        # class variables
        self.filehandler = IOhandler
        self.url = url
        self.nesting_tags = 0
        self.data = []
        # html tags to search for
        self.tag = 'div'
        self.name = 'class'
        self.value = 'temp fact__temp'

    # Using the HTMLParser to search for the needed tag in this case 'temp fact__temp'
    # Then checking all the nested tags and retrieving the temperature data.

    def handle_starttag(self, tag, attributes):
        if tag != self.tag:
            return
        if self.nesting_tags:
            self.nesting_tags += 1
            return
        for name, value in attributes:
            if name == self.name and value == self.value:
                break
        else:
            return
        self.nesting_tags = 1

    def handle_endtag(self, tag):
        if tag == self.tag and self.nesting_tags:
            self.nesting_tags -= 1

    def handle_data(self, data):
        if self.nesting_tags:
            self.data.append(data)

# -----------------------------------------------------------

    def get_weather(self):
        # get webpage html
        http_response = urllib.request.urlopen(self.url)
        http_response.info()
        html = http_response.read()

        # parse with html
        self.feed(str(html))

        # return current temperature
        return int(self.data[0])

