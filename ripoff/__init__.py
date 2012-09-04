from ripoff import distances
from ripoff.clustering import dendrogram
import numpy

__all__ = ['all_pairs', 'dendrogram', 'distances']

def _worker(x):
    '''special private worker function that needs to be importable
    i and j are indices which need to be conserved in the return value'''
    (f, i, j, a, b, kw) = x
    return i, j, f(a, b, **kw)


def all_pairs(catalogue, distance=distances.combined, dist_kwargs=None, parallel=False):
    """Generate the all-pairs distance matrix for all elements in catalogue

    distance: any distance function that accepts two words and
        returns a similarity value between 0 and infinity
    dist_kwargs:
        additional kwargs for the distance function
    parallel: use a Pool from the multiprocessing module for
        parallel computation
    """
    if not dist_kwargs: dist_kwargs = dict()
    # Initialize all-pairs matrix
    M = numpy.zeros((len(catalogue), len(catalogue)), dtype=numpy.float32)

    if parallel:
        from multiprocessing import Pool
        p = Pool()
        for (i, j, d) in p.map(_worker,
            ((distance, i, j, catalogue[i], catalogue[j], dist_kwargs)
                for i in (range(0, len(catalogue)))
                    for j in (range(i + 1, len(catalogue))))):
            M[i][j] = M[j][i] = d
    else:
        for i in range(len(catalogue)):
            for j in range(i + 1, len(catalogue)):
                M[i][j] = M[j][i] = distance(catalogue[i], catalogue[j])

    return M

