from warnings import warn
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import matplotlib
    matplotlib.use('Agg')  # Only backend available in server environments
    import matplotlib.pylab as pylab
except ImportError as e:
    warn('%s: Rendering of diagrams is not possible' % e.message)
    matlpotlib = pylab = False
import hcluster
#import ripoff


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
