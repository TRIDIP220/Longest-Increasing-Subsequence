def fun(arr):
	n = len(arr)
	a = [1]*n
	for i in range (1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and a[i]< a[j] + 1 :
				a[i] = a[j]+1
	mx = 0

	for i in range(n):
		mx = max(mx, a[i])
	return mx

arr = [10,9,2,5,3,7,101,18]
print(fun(arr))

#Time complexity is o(n^) as here has a nested loop
#space complecity is o(n) as only one array is use to store the value