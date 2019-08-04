from urllib.request import Request, urlopen
from html.parser import HTMLParser


# Create new parser by overriding the HTMLParser class
class MyHTMLParser(HTMLParser):

    # Initializing lists
    lsStartTags = list()
    lsEndTags = list()
    lsStartEndTags = list()
    lsComments = list()

    # HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        self.lsStartTags.append(startTag)

    def handle_endtag(self, endTag):
        self.lsEndTags.append(endTag)

    def handle_startendtag(self,startendTag, attrs):
        self.lsStartEndTags.append(startendTag)

    def handle_comment(self,data):
        self.lsComments.append(data)


# request using known browser agent
req = Request('http://ordergroove.com/company', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# convert HTML content from bytes to string
html_str = webpage.decode("utf8")

# Instantiate a new parser object
parser = MyHTMLParser()

# Feed new parser HTML content
parser.feed(html_str)

# Q1) Display total qty. of HTML elements
complete_count = 0
for start_tag in parser.lsStartTags:
    # Count number of matching tags
    if start_tag in parser.lsEndTags:
        complete_count += 1
print("Total number of HTML elements: "+str(complete_count))


# Q2) Display top 5 most frequently used HTML tags & their respective counts

# write to file
# with open("og_site.html", "w") as new_file:
#     new_file.write(str(tags))
