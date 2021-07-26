#Charlene Crystal Namuyige 
#Practice for Coding Interviews 

#Binary Search Algorithm 
#has to be sorted 
#recursive approach

#returns the index of the number searched for
def BinarySearch(arr, num, start, end):
    mid = (start + end)//2

    if end >= start:
        if num ==  arr[mid]:
            return mid; 
        elif num < arr[mid]:
            return BinarySearch(arr, num, start, mid - 1)
        else:
            return BinarySearch(arr, num, mid + 1, end)
    return -1 
             

arr = [1, 2, 3, 4, 5, 6, 7]

target = 3
start = 0
end = len(arr) - 1

index = BinarySearch(arr, target, start, end)

if index != -1: 
    print(f'The index your search number is at is at', index )
else:
    print("Your search number is not here")
