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


# Request using known browser agent
req = Request('http://ordergroove.com/company', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Convert HTML content from bytes to string
html_str = webpage.decode("utf8")

# Instantiate a new parser object
parser = MyHTMLParser()

# Feed new parser HTML content
parser.feed(html_str)

# QUESTION #1) Display total qty. of HTML elements
#
#
# Count quantity of matching start/end tag pairs
complete_count = 0
for start_tag in parser.lsStartTags:
    if start_tag in parser.lsEndTags:
        complete_count += 1
print("\nQUESTION #1: \n" + "    Total number of HTML elements: "+str(complete_count) + "\n")

# QUESTION #2) Display top 5 most frequently used HTML tags & their respective counts
#
#
# Aggregate all tags
all_tags = parser.lsStartTags + parser.lsEndTags

# Create map to hold count of each tag
tag_map = {}
for tag in all_tags:
    if tag not in tag_map:
        tag_map[tag] = 1
    else:
        tag_map[tag] += 1

# Sort tag counts in ascending order
asc_tag_count = sorted(list(tag_map.values()))

# Create dict of the top 5 tag counts and their respective tags
top_5_tag_values = asc_tag_count[-5:]
top_5_tags = {}
for val in top_5_tag_values:
    for tag in tag_map:
        if tag_map[tag] == val and val not in top_5_tags:
            top_5_tags[val] = tag

# Display results
print("QUESTION #2:")
for count in top_5_tags:
    print("    '" + top_5_tags[count] + "' was detected " + str(count) + " number of times.")
