#Task1: Print two list with odd numbers in one list and even numbers in another list
print("Program to print two lists with odd numbsers in one list and even numbers in another list:")
print("")
print("                ****************************                 ")
print("")
#get the list
list_given= [10,501,22,37,100,999,87,351]
print("Given list: ",list_given)
#initialize two list (odd n even)
list_odd=[]
list_even=[]
#using for loop iterate the list
for num in list_given:
    #using if condition check the odd or even
    if num % 2 == 0:
       list_even.append(num)
    else:
       list_odd.append(num)
print("List of even numbers are: ", list_even)
print("List of odd numbers are: ", list_odd)
print("\n")
print("--------------------------------------------------------------------")
print("")

#Task2: Count prime numbers and print new python list contains only prime numbers
print("Program to print list of prime numbers:")
print("")
print("                ****************************                 ")
print("")
# Given number list
print(" The given number of list is: ", list_given)
 
# Empty list
ansList = []
 
# Iterate through each number 
# form the list
for num in list_given :
     
    # 0 and 1 is not a 
    # prime number
    # so skip this number
    if num == 0 or num == 1 :
        continue
         
    # loop from 2 to half of the
    # given number
    for i in range(2, num // 2 + 1) :
 
        # If number is divisible by any
        # number (i) then it is not
        # a prime number
        if num % i == 0 :
            break
 
    # If not divisible then it is
    # a prime number
    else :
         
        # if number is prime
        # then append to the list
        ansList.append(num)
 
# If list is non-empty then
# print th elements
if len(ansList) :
     
    print("Prime Number : ", ansList)
     
    # printing the prime number
    # from the ansList
       
else :
    print("No any number from the given list is Prime")
print ("Total number of prime numbers in the given list : ", len(ansList))
print("")
print("--------------------------------------------------------------------")
print("")

#Task3: To find the happy numbers in given python list
print("Program to find the happy numbers in given python list:")
print("")
print("                ****************************                 ")
print("")
# Given number list
print(" The given number of list is: ", list_given)
 
# Empty list
#ansList = []
#for num in list_given :





print("")
print("--------------------------------------------------------------------")
print("")

#Task4: To find the sum of first and last digit of an integer
print("Program to find the sum of first and last digit of an integer:")
print("")
print("                ****************************                 ")
print("")
def sum_of_first_and_last_digit(n):
    # convert the input number to a string
    str_n = str(n)
     
    # extract the first and last digit
    first_digit = int(str_n[0])
    last_digit = int(str_n[-1])
     
    # add the first and last digit
    sum = first_digit + last_digit
     
    # return the sum
    return sum
n = 153
print("The given number is: ", n)
result = sum_of_first_and_last_digit(n)
print("sum of first and last digit of an integer is: ", result)
print("")
print("--------------------------------------------------------------------")
print("")

#Task6: To find the duplicates numbers in given python list
print("Program to find the duplicate numbers in given python list:")
print("")
print("                ****************************                 ")
print("")
# the original list of integers with duplicates
mylist = [10, 5, 6, 9, 12, 6, 5, 66, 6, 11, 2] 
print("Given number of list is: ", mylist)
# empty list to hold unique elements from the list
newlist = [] 
# empty list to hold the duplicate elements from the list
duplist = [] 
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        # this method catches the first duplicate entries, and appends them to the list
# The next step is to print the duplicate entries, and the unique entries
        duplist.append(i) 
print("Duplicate numbers in the given list is: ", duplist)

print("")
print("--------------------------------------------------------------------")
print("")

#Task7: To find the duplicates numbers in given python list
print("Program to find the duplicate numbers in given python list:")
print("")
print("                ****************************                 ")
print("")
def firstNonRepeating(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1
 
 
# Driver code
arr = [10, 5, 9, 5, 55, 10]
n = len(arr)
print("Duplicate number in the list: ", firstNonRepeating(arr, n))
print("")
print("--------------------------------------------------------------------")
print("")

#Task8: To find the minimum element in a rate and sorted list
print("Program to find the minimum element in a rate and sorted list:")
print("")
print("                ****************************                 ")
print("")
list1 = [62, 34, 5, 91, 1, 11]
print("Given list is: ", list1)
# sorting the list
list1.sort()
 
# printing the first element
print("Minimum element in a given list:", list1[0])
print("")
print("--------------------------------------------------------------------")
print("")


