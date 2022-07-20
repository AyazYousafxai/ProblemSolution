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


n=7
startIndex=0
outputArray=[]
# inputArray= [12, 1, 2, 3, 0, 11, 4]
inputArray=[1, 2, 3, 4, 2]
sol=Solution()
sol.constructLowerArray(inputArray,startIndex,outputArray)
print(outputArray)