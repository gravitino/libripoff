'''Test suite module for the all_pairs function

@since: 2012-09-11
@author: moschlar
'''

from __future__ import absolute_import

import unittest

import numpy as np
from ripoff import all_pairs, distances


class TestAllPairs(unittest.TestCase):

    catalogue = ["""
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
    all_pairs = np.array([
        [0.0, 0.09557109326124191, 0.20822621881961823, 0.41584157943725586],
        [0.09557109326124191, 0.0, 0.1149425283074379, 0.3932584226131439],
        [0.20822621881961823, 0.1149425283074379, 0.0, 0.3164556920528412],
        [0.41584157943725586, 0.3932584226131439, 0.3164556920528412, 0.0]
    ])

    def test_all_pairs_sequential(self):
        '''Test if sequential version of all_pairs works'''
        p = all_pairs(self.catalogue)
        np.testing.assert_array_equal(p, self.all_pairs)

    def test_all_pairs_parallel(self):
        '''Test if parallel version of all_pairs works'''
        p = all_pairs(self.catalogue, parallel=True)
        np.testing.assert_array_equal(p, self.all_pairs)

    def test_all_pairs_equality(self):
        '''Test if parallel and sequential version of all_pairs deliver equal results'''
        p = all_pairs(self.catalogue).tolist()
        pp = all_pairs(self.catalogue, parallel=True).tolist()
        np.testing.assert_array_equal(p, pp)

    def test_all_pairs_unicode(self):
        '''Test all_pairs with strange unicode characters'''
        all_pairs(['ae', u'\xc3\xa4', 'ss', u'\xc3\x9f'])

    def test_all_pairs_empty(self):
        '''Test all_pairs with empty input'''
        all_pairs(['Something', 'nothing', ''])

    def test_all_pairs_kwargs(self):
        '''Test kwargs acceptance of all_pairs'''
        all_pairs(self.catalogue, distance=distances.jaccard, dist_kwargs=dict(mode=2))
        all_pairs(self.catalogue, dist_kwargs=dict(jaccard_mode=2))
