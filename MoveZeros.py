#Given an array of integers, write a function to move all 0's to the end 
#while maintaining the relative order of rest of the elements 

#Algorithm -- moving all numbers ahead
#setting the rest of the numbers in the list to 0

def Move_Zeros(arr, length):

    j = 0
    for num in arr:
        if num != 0:
            arr[j] = num
            j = j + 1
    print(j)
    print(length)

    for num in range(j,length):
        arr[num] = 0

arr = [1, 0, 4, 0, 12]
length = len(arr)
print(arr)
Move_Zeros(arr, length)
print("After the function")
print(arr)