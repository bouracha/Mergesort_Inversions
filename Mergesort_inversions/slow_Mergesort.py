import time


def Mergesort_Inversions(A):
    num_inversions = 0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if(A[i] > A[j]):
                num_inversions += 1
    return num_inversions




### Main ###
A = []

result_file = r'input.txt'
with open(result_file) as file:
    data_array = [[float(digit) for digit in line.split()] for line in file]

for i in range(0, len(data_array)):
    A.append(data_array[i][0])

start_time = time.time()

num_inversions = Mergesort_Inversions(A)

end_time = time.time()
print "Runtime: ", (end_time - start_time), " seconds."

print "Number of Inversions: ", num_inversions
