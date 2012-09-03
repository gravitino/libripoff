import urllib2


catalogue = []


urls = ["http://www.gutenberg.org/files/21000/21000-0.txt",    # faust 1
        "http://www.gutenberg.org/cache/epub/2230/pg2230.txt", # faust 2
        "http://www.gutenberg.org/cache/epub/6649/pg6649.txt"] # schiller

for url in urls:

    catalogue.append(urllib2.urlopen(url).read())


print catalogue
