from urllib.request import Request, urlopen
from html.parser import HTMLParser


# Create new parser by overriding the HTMLParser class
class MyHTMLParser(HTMLParser):
    """
    Class inherits the HTMLParser class and overrides it to generate lists of all the
    start and end tags.
    """

    # Intialize lists
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


def element_counter(start_tags, end_tags):
    """
    Function will generate a count of all matching start & end tag pairs. This count is
    indicative of the total quantity of elements.
    :param start_tags:
    :param end_tags:
    :return: Integer representing total quantity of elements.
    """
    complete_count = 0
    for start_tag in start_tags:
        if start_tag in end_tags:
            complete_count += 1
    return complete_count


def tag_counter(start_tags, end_tags):
    """
    Function will determine how many times each tag was used and store each tag and its
    respective count in a dictionary.
    :param start_tags: List of all starting tags.
    :param end_tags: List of all ending tags.
    :return: tag_map: Dictionary
    """
    # Aggregate all tags
    all_tags = parser.lsStartTags + parser.lsEndTags
    # Create map to hold count of each tag
    tag_map = {}
    for tag in all_tags:
        if tag not in tag_map:
            tag_map[tag] = 1
        else:
            tag_map[tag] += 1
    return tag_map


def top_5_tag_finder(tag_map):
    """
    Function accepts a map of each HTML tag and its count, and returns a dictionary containing the
    top 5 most frequently used tags, in which the counts are the keys, and the tags are the values.
    :param tag_map: Dictionary containing all HTML tags as keys and their respective counts as values.
    :return: top_5_tags: Dictionary of top 5 most frequently used tag counts and their tag values.
    """
    # Sort tag counts in ascending order
    asc_tag_count = sorted(list(tag_map.values()))

    # Create dict of the top 5 tag counts and their respective tags
    top_5_tag_values = asc_tag_count[-5:]
    top_5_tags = {}
    for val in top_5_tag_values:
        for tag in tag_map:
            if tag_map[tag] == val and val not in top_5_tags:
                top_5_tags[val] = tag
    return top_5_tags


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
element_count = element_counter(parser.lsStartTags, parser.lsEndTags)

# QUESTION #2) Display top 5 most frequently used HTML tags & their respective counts
tag_map = tag_counter(parser.lsStartTags, parser.lsEndTags)
top_5_tags = top_5_tag_finder(tag_map)

# Display results
print("\nQUESTION #1: \n" + "    Total number of HTML elements: "+str(element_count) + "\n")
print("QUESTION #2:")
for count in top_5_tags:
    print("    '" + top_5_tags[count] + "' was detected " + str(count) + " number of times.")
