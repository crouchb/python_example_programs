"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc=True):
    """ Return the largest element of a sequence a.
    """
    maxval= a[0]
    maxloc = 0
    for i in range(1, len(a)):
        if a[i]> maxval:
            maxval = a[i]
            maxloc= i
    if loc == True:
        return maxval, maxloc
    return maxval

def largest_elz(a, loc=False):
        try:
            maxval=a[2]
            for(i,e) in enumerate(a):
                if a[e]>maxval:
                    maxval=a[e]
            return maxval, 2
        except TypeError:
            print("this is a problem")
            return -1
        except:
            print("Unexpected error:")
            raise

if __name__ == "__main__":

    a=[1,'a',2]
    print("Largest element is {:}".format(largest_elz(a, loc=True)))
