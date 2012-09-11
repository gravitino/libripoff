'''The all_pairs method for sequential and parallel usage

@author: moschlar
'''

from __future__ import absolute_import

import numpy
from ripoff import distances

__all__ = ['all_pairs']


def _worker(x):
    '''special private worker function that needs to be importable'''
    (f, a, b, kw) = x
    return f(a, b, **kw)


def all_pairs(catalogue, distance=distances.combined, dist_kwargs=None, parallel=False):
    """Generate the all-pairs distance matrix for all elements in catalogue

    distance: any distance function that accepts two words and
        returns a similarity value between 0 and infinity
    dist_kwargs:
        additional kwargs for the distance function
    parallel: use a Pool from the multiprocessing module for
        parallel computation
    """
    dist_kwargs = dist_kwargs or dict()
    # Initialize all-pairs matrix
    M = numpy.zeros((len(catalogue), len(catalogue)), dtype=numpy.float32)

    indices = [(i, j) for i in range(len(catalogue)) for j in range(i + 1, len(catalogue))]

    if parallel:
        from multiprocessing import Pool
        p = Pool()
        for (i, j), d in zip(indices, p.map(_worker,
            ((distance, catalogue[i], catalogue[j], dist_kwargs)
                for i, j in indices))):
            M[i][j] = M[j][i] = d
    else:
        for i, j in indices:
            M[i][j] = M[j][i] = distance(catalogue[i], catalogue[j])

    return M
