from urllib.request import Request, urlopen

req = Request('http://ordergroove.com/company', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

print(webpage)