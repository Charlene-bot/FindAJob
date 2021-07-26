#Charlene Crystal Namuyige 
#Given an array of integers of size N, find maximum sum of K consequtive elements 


#arr = array 
#k = number of consequetive elements to check 
#length of array
def window_sum(arr, k, n):
    #find the sum of the first window
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum

    #loop through 
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k] 
        max_sum = max(max_sum, window_sum)
    
    return max_sum

    
arr = [10, 3, 4, 3]
length = len(arr)
k = 2 
max = window_sum(arr, k, length)
#Print the outcome 
print(f'The maximum sum of consequtives is', max)