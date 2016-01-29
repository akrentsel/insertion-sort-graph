# Insertion Sort Graph
Animated, graphical view of the way that insertion sort works on a random set of (integer) data.

# Explanation

The idea behind insertion sort is that for every element that we see, we take it and move it to its place in the part of the list that we've gone through so far. To do this, we begin iterating through the list. For every element, we compare that element to the item directly to its left. If the element directly to the left is bigger, we swap the two, and compare again with the new left element. This continues until the item to the left of the element we are moving is less than or equal to the element that we are moving. At that point, we return back to the point where the first swap occured and continue iterating through the rest of the list.

An important point to note is that once we hit an element in our iteration that we are going to begin swapping, we need to save a pointer to where we start swapping so we can return there once we are done swapping.

# Runtime

The worst case is O(N^2)

This happens if we are given a list to sort that is in reverse order.

Then, we have to move the element through the entire "locally sorted" section of the list every time, so for an input list of length n that is in reverse order, we take

(1 + 2 + 3 + ... n - 1)

swaps to sort the list, which is O(n^2) runtime.

In the best case, if the list is already sorted, we get O(n^2) runtime.

For a random set of data, this isn't the fastest sort, but it is a good sort to choose if we are given a list that is "almost" sorted. Then we have runtime near O(N). A list is "almost sorted" is it needs a relatively small number of swaps to become in sorted order.

# Example

To walk through an example:

We start with a list of numbers:

[5, 3, 6, 2, 1]

First, we look at the first item (denoted by ^) and compare it to its left neighbor.

[5, 3, 6, 2, 1] <br>
 ^

In this case, the first element has no left neighbor, so it is automatically in the right place.
Then we look at the next element, and compare it to the previous element. 

[5, 3, 6, 2, 1]<br>
    ^

5 is greater than 3, so we remember the point that we were at (denoted by *) so we can return later, and swap.

[3, 5, 6, 2, 1] <br>
 ^	*

 There is no element to the left of 3, so that part of the list ([3, 5]) is now in "local" order. So we return to our saved position and move on to the next element.

 [3, 5, 6, 2, 1]<br>
        ^

6 is geater than 5, so we have nothing to move.

[3, 4, 6, 2, 1]<br>
          ^

2 is less than 6, so we need to swap. We mark the location and begin swapping. 

[3, 4, 2, 6, 1]<br>
   	   ^  *

[3, 2, 4, 6, 1]<br>
   	^     *

[2, 3, 4, 6, 1]<br>
 ^ 	      *

 We get to the end, jump back to the pointer + 1, and repeat the process with 1.

[2, 3, 4, 1, 6]<br>
          ^  *

...

[1, 2, 3, 4, 6]

And the list is sorted!

# Implementation Details and Requirements

You must have numpy and matplotlib installed to run this animation. 

