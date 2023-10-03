# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	swapped = False
	# Traverse through all array elements using for
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:    #swapping elements
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return


# Driver code to test above
arr = [68, 70, 25, 19, 2, 7, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
