# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [10, 9, 11, 3, 4]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

# This code is contributed by Mohit Kumra
