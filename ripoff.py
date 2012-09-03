import numpy
import difflib


def segmentation(source, mode=0):
    """segmentation of a given string via shingling or splitting"""

    # if shingling length is zero return naive segmentation via split
    if mode == 0:
        return source.split()

    # else compute shingling list with maximum word length of "mode"
    else:

        result = []

        for length in range(1, mode + 1):
            for index in range(len(source) - length):
                result.append(source[index: index + length])

        return result


def dist_jaccard(source0, source1, mode=0):
    """popular similarity measure for two given sets"""

    # calculate shingling sets
    set0 = set(segmentation(source0, mode=mode))
    set1 = set(segmentation(source1, mode=mode))

    union = set0.union(set1)
    inter = set0.intersection(set1)

    return float(len(union) - len(inter)) / len(union)


def dist_difflib(source0, source1):
    """popular Gestalt-algorithm implemented in difflib"""

    match = difflib.SequenceMatcher(a=source0, b=source1)

    return 1 - match.ratio()


def dist_combined(source0, source1):
    """combine all approaches to find different types of plagiarism"""

    return min(dist_jaccard(source0, source1, 0),
               dist_jaccard(source0, source1, min(len(source0), len(source1))),
               dist_difflib(source0, source1))


if __name__ == '__main__':
    print dist_combined(
        "mooo maaa miiiiii lalalala",
        "lalalala mooo maaa miiiiii")
