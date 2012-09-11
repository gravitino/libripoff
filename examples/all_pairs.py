'''Some basic example calls for the all_pairs method'''

from ripoff import all_pairs, distances
#import pickle

if __name__ == '__main__':

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
    print all_pairs(catalogue)
    print all_pairs(catalogue, parallel=True)
    print all_pairs(catalogue, distance=distances.kolmogorov)

# Example code for loading a pickle file of submissions

#    d = pickle.load(open('submissions.pkl'))
#
#    for a in (a for a in d if a['submissions']):
#        catalogue = [s['source'] for s in a['submissions'] if s['source']]
#        print all_pairs(catalogue, parallel=True)
