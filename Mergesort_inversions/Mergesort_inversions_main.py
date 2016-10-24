import time

def Mergesort_Inversions(A):
    n = len(A)
    if (n == 1):
        return A, 0
    else:
        #print "Splitting: ", A, " into:"
        mid = len(A)//2
        B = A[:mid] ##lefthalf array
        C = A[mid:] ##righthalf array
        #print B
        #print C
        B, x = Mergesort_Inversions(B)
        C, y = Mergesort_Inversions(C)
        D, z = CountSplitInversions(B, C)

        return D, (x+y+z)


def CountSplitInversions(B, C):
    i = j = 0
    num_inversions = 0
    D = []
    #print "Count inversions between:", B, C
    while i < len(B) and j < len(C):
        if (B[i] <= C[j]) and (i < len(B)):
            D.append(B[i])
            i += 1
        elif B[i] > C[j]:
            D.append(C[j])
            #print "Inversion(s) Found!"
            num_inversions += len(B) - (i)
            j += 1

    while i == len(B) and j < len(C):
        D.append(C[j])
        j += 1

    while i < len(B) and j == len(C):
        D.append(B[i])
        i += 1

    #print "Return sorted: ", D, " with ", num_inversions, " inversion"
    return D, num_inversions



### Main ###

#A = [4,3,2,1,3,9,6,1,7]
A = []

result_file = r'input.txt'
with open(result_file) as file:
    data_array = [[float(digit) for digit in line.split()] for line in file]

for i in range(0, len(data_array)):
    A.append(data_array[i][0])

#print "Input array: ", A

start_time = time.time()

A, num_inversions = Mergesort_Inversions(A)

end_time = time.time()
print "Runtime: ", (end_time - start_time), " seconds."

#print "Sorted array: ", A, " with ", num_inversions, " inversions."
print "Number of inversions: ", num_inversions