"""
CSCI 355 Project 1
Chai Grindean


BubbleSort
Time Complexity: O(n^2)
"""
def BubbleSort(num_list):
    for i in range (0, len(num_list)-1): #Outer Loop,i counter, range from 0 to n-1
        for j in range(0, len(num_list) -1 - i): #Inner Loop, j (list element counter) range from 0 to n-1-i
            if num_list[j] < num_list[j+1]: #If number on the left is less than number on the right
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j] #they swap places
                print(num_list) #shows process at each step
    return num_list #returns the now sorted list.

testList = [4, 5, 7, 9, 1, 3, 2, 6, 0, 8] #testList to test Function

print ("List of Numbers: ",'\n',testList)
print("Sorted List of Numbers: ",'\n',BubbleSort(testList)) #Program Successful!










