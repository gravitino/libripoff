import bz2
import numpy
import difflib

def _worker(x):
    '''special private worker function that needs to be importable
    i and j are indices which need to be conserved in the return value'''
    (f, i, j, a, b, kw) = x
    return i, j, f(a, b, **kw)

def segmentation(source, mode=1):
    """segmentation of a given string via shingling or splitting"""

    segments = source.split()

    # compute shingling list with maximum word length of "mode"
    result = []

    for length in range(1, mode + 1):
        for index in range(len(segments) - length):
                result.append(tuple(segments[index: index + length]))

    return result


def dist_jaccard(source0, source1, mode=1):
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

def dist_kolmogorov(source0, source1):
    """approximate Kolmogorov distance via compression"""

    comp01 = len(bz2.compress(source0))
    comp10 = len(bz2.compress(source1))
    comp11 = len(bz2.compress(source0 + source1))
    
    return float(comp11 - min(comp01, comp10)) / max(comp01, comp10)

def dist_combined(source0, source1):
    """combine all approaches to find different types of plagiarism"""

    return min(dist_jaccard(source0, source1, 1),
               dist_difflib(source0, source1),
               dist_kolmogorov(source0, source1))

def all_pairs(catalogue, distance=dist_combined, dist_kwargs=None, parallel=False):
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


if __name__ == '__main__':

    catalogue = [
"""
public class HelloWorld {
    // A program to display the message
    // "Hello World!" on standard output

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}   // end of class HelloWorld
""", """
public class HelloWorld {
    // A program to display the message

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}   // end of class HelloWorld
""", """
public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}   // end of class HelloWorld
""", """
public class HelloUniverse {

    public static void main(String[] args) {
        String message = "Hello World!";
        System.out.println(message);
    }
}
"""]
    print all_pairs(catalogue)
    print all_pairs(catalogue, parallel=True)
    print segmentation(catalogue[0])


