
unsortedArr = [20,90,50,80,30,100,10,70,40]



def partition(unsortedArr):
  pivotNumber = unsortedArr[len(unsortedArr)-1]
  i = -1
  j = 0
  greaterThanPivotArr = []
  lessThanPivotArr = []
  while(j < len(unsortedArr)-1):
    if(unsortedArr[j] < pivotNumber):
      i=+1
      lessThanPivotArr.append(unsortedArr[j])
      j+=1
    elif(unsortedArr[j] > pivotNumber):
      greaterThanPivotArr.append(unsortedArr[j])
      j+=1
  
  print("less than arr" + str(lessThanPivotArr))
  print("greater than arr" + str(greaterThanPivotArr))
  print("og array" + str(unsortedArr))

partition(unsortedArr)



    

