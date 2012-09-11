'''libripoff main module

@since 2012-09-11
@author: moschlar
'''

from __future__ import absolute_import

from ripoff.all_pairs import all_pairs
from ripoff import distances
from ripoff.clustering import cluster, dendrogram

__all__ = [
    'all_pairs',
    'distances',
    'cluster', 'dendrogram'
]