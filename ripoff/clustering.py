'''
If you want to use the dendrogram function in a server environment,
you have to make sure you load the 'Agg' backend for matplotlib
*before* importing this module!

I.e. you have to do something like:

    import matplotlib
    matplotlib.use('Agg')  # Only backend available in server environments
    from ripoff import dendrogram

@author: moschlar
'''

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

import pylab
import hcluster


def cluster(M, method='complete'):
    return hcluster.linkage(hcluster.squareform(M), method=method)


def dendrogram(M, method='complete', **kw):
    s = StringIO.StringIO()
    if pylab:
        try:
            pylab.figure()
            pylab.title('complete linkage clustering')
            hcluster.dendrogram(cluster(M, method), **kw)
        except:
            pass
        else:
            pylab.savefig(s, format='png')
            s.seek(0)
        finally:
            pylab.close()
    return s
