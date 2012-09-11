'''
This example shows how to cluster the all_pairs distance matrix
as a dendrogram figure with the help of hcluster.

Some classical german literature is used as dummy data, but it
shows interesting thought expectable results.

*Important:*
This is an example for using pylab interactively with a GUI!
If you want to use the dendrogram as a plain image file
(e.g. for serving the image on a web page), refer to the comment
in the file ripoff/clustering.py for instructions on how to configure
the correct matplotlib backend.

@author: gravitino
'''

from ripoff import all_pairs, distances
from ripoff.clustering import cluster
import urllib2
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
        ("http://www.gutenberg.org/files/26686/26686-0.txt",      "Birnbaum"),
        ("http://www.gutenberg.org/files/21593/21593-0.txt",      "Urteil"),
        ("http://www.gutenberg.org/cache/epub/22367/pg22367.txt", "Verwand.")]

# get it from the interwebs
catalogue = []

for url, name in urls:
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, None, headers)
    catalogue.append(urllib2.urlopen(req).read())

# calc similarity matrix
M = all_pairs(catalogue,
    distance=distances.jaccard,
    dist_kwargs=dict(mode=1),
    parallel=True)

# plot similarity matrix
pylab.figure(1)
pylab.title("similarity matrix")
pylab.imshow(M, aspect='auto', interpolation="nearest", cmap="Reds")
pylab.colorbar()

# plot complete linkage
pylab.figure(2)
pylab.title("complete linkage clustering")
hcluster.dendrogram(cluster(M, method='complete'), leaf_label_func=lambda i: urls[i][1])

# finally show
pylab.show()
