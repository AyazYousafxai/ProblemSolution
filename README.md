# Problem 1
## Print count of repeating string in python
```
e.g 
problem = ['a','a','a','a','b','c','c','d','d','ayaz','ayaz','shaheroom','ayaz']
output = ['a_1', 'a_2', 'a_3', 'a_4', 'ayaz_1', 'ayaz_2', 'ayaz_3', 'c_1', 'c_2', 'd_1', 'd_2']
```
### Solution
```
repeated.py
```
# Problem 2
#### Given an array Arr of size N containing positive integers. Count number of smaller elements on right side of each array.

##### Example
```
Input:
N = 7
Arr[] = {12, 1, 2, 3, 0, 11, 4}
Output: 6 1 1 1 0 1 0
Explanation: There are 6 elements right
after 12. There are 1 element right after
1. And so on.
```
### Solution
```
file name
count_right_element.py
```
```
class Solution:
    def countLower(self,outputArray,inputArray,startIndex,compareElement):
        counter=0
        for i in inputArray[startIndex+1:]:
            if compareElement>i:
                counter+=1

        outputArray.append(counter)
    def constructLowerArray(self,inputArray,startIndex,outputArray):
        if startIndex<len(inputArray):
            compareElement=inputArray[startIndex]
        
            self.countLower(outputArray,inputArray,startIndex,compareElement)
            startIndex+=1
            self.constructLowerArray(inputArray,startIndex,outputArray)


startIndex=0
outputArray=[]
# inputArray= [12, 1, 2, 3, 0, 11, 4]
inputArray=[1, 2, 3, 4, 2]
sol=Solution()
sol.constructLowerArray(inputArray,startIndex,outputArray)
print(outputArray)
```
