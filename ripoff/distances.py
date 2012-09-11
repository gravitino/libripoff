'''Different distance measures for use in the all_pairs function

@author: gravitino
'''

import bz2
import difflib

__all__ = ['jaccard', 'gestalt', 'kolmogorov', 'combined']


def segmentation(source, mode=1):
    """segmentation of a given string via shingling or splitting"""

    segments = source.split()

    # compute shingling list with maximum word length of "mode"
    result = []

    for length in range(1, mode + 1):
        for index in range(len(segments) - length):
                result.append(tuple(segments[index: index + length]))

    return result


def jaccard(source0, source1, mode=1):
    """popular similarity measure for two given sets"""

    # calculate shingling sets
    set0 = set(segmentation(source0, mode=mode))
    set1 = set(segmentation(source1, mode=mode))

    union = set0.union(set1)
    inter = set0.intersection(set1)

    if len(union) == 0:
        return float("infinity")

    return float(len(union) - len(inter)) / len(union)


def gestalt(source0, source1):
    """popular Gestalt-algorithm implemented in difflib"""

    match = difflib.SequenceMatcher(a=source0, b=source1)

    return 1 - match.ratio()


def kolmogorov(source0, source1):
    """approximate Kolmogorov distance via compression"""
    source0, source1 = source0.encode('utf-8'), source1.encode('utf-8')

    comp01 = len(bz2.compress(source0))
    comp10 = len(bz2.compress(source1))
    comp11 = len(bz2.compress(source0 + source1))

    return float(comp11 - min(comp01, comp10)) / max(comp01, comp10)


def combined(source0, source1, jaccard_mode=1):
    """combine all approaches to find different types of plagiarism"""

    return min(jaccard(source0, source1, jaccard_mode),
               gestalt(source0, source1),
               kolmogorov(source0, source1))
