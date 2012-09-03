import urllib2
import ripoff
import hcluster
import pylab

# some famous German literature
urls = [("http://www.gutenberg.org/files/21000/21000-0.txt",      "Faust 1"),
        ("http://www.gutenberg.org/cache/epub/2230/pg2230.txt",   "Faust 2"),
        ("http://www.gutenberg.org/cache/epub/6498/pg6498.txt",   "Kabale"),
        ("http://www.gutenberg.org/cache/epub/6383/pg6383.txt",   "Orleans"),
        ("http://www.gutenberg.org/cache/epub/6079/pg6079.txt",   "Winterma."),
        ("http://www.gutenberg.org/cache/epub/24249/pg24249.txt", "Harzreise"),
        ("http://www.gutenberg.org/cache/epub/7205/pg7205.txt",   "Zarathus."),
        ("http://www.gutenberg.org/cache/epub/7202/pg7202.txt",   "Ecce Homo"),
        ("http://www.gutenberg.org/cache/epub/5323/pg5323.txt",   "Effi Bri."),
        ("http://www.gutenberg.org/files/26686/26686-0.txt",      "Birnbaum" ),
        ("http://www.gutenberg.org/files/21593/21593-0.txt",      "Urteil"),
        ("http://www.gutenberg.org/cache/epub/22367/pg22367.txt", "Verwand.")]

# get it from the interwebs
catalogue = []

for url, name in urls:

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request(url, None, headers)
    catalogue.append(urllib2.urlopen(req).read())


# get similarity matrix
M = ripoff.all_pairs(catalogue, 
                     distance=ripoff.dist_jaccard, dist_kwargs={'mode': 1}, 
                     parallel=True)

# plot similarity matrix
pylab.figure(1)
pylab.title("similarity matrix")
pylab.imshow(M, aspect = 'auto', interpolation = "nearest", cmap = "Reds")
pylab.colorbar()

# plot complete linkage
pylab.figure(2)
pylab.title("complete linkage clustering")
hcluster.dendrogram(hcluster.linkage(hcluster.squareform(M), method='complete'), 
                    leaf_label_func=lambda i: urls[i][1])

# finally show
pylab.show()
