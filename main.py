# Merge Sort citation: https://www.programiz.com/dsa/merge-sort#google_vignette
# Insertion Sort citation: https://www.programiz.com/dsa/insertion-sort
import random
import timeit
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1



def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()







n = 65
start = timeit.default_timer()
print("The start time is :", start)
for i in range(1000):
    insertionSort(random.sample(range(0,1000), n))
print("The difference of time is :",
              timeit.default_timer() - start)
start2 = timeit.default_timer()
print("The start2 time is :", start2)
for i in range(1000):
    mergeSort(random.sample(range(0,1000), n))
print("The difference2 of time is :",
              timeit.default_timer() - start2)
