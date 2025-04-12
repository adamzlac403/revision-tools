unsortedArr = [20,90,50,80,30,100,10,70,40]
def partition(unsortedArr,pivotIndex):
  
  pivotNum = unsortedArr[pivotIndex]
  
  print("pivot number " + str(pivotNum))
  
  i = -1
  j = 0
  print (str(len(unsortedArr)))
  while(j < len(unsortedArr) - 1):
    print("in while")
    print("unsorted arr j" + str(unsortedArr[j]))
    if (unsortedArr[j] < pivotNum):
      print("if hit")
      i+=1
      print("unsorted arr j: " + str(unsortedArr[j]))
      print("unsorted array i = "+ str(unsortedArr[i]))
      unsortedArr[i],unsortedArr[j] = unsortedArr[j],unsortedArr[i]
      print(str(unsortedArr))
      j+=1
    elif (unsortedArr[j] > pivotNum):
      print("elif hit")
      j+=1
  unsortedArr[i+1], unsortedArr[len(unsortedArr)-1] = unsortedArr[len(unsortedArr)-1],unsortedArr[i+1]
  print(unsortedArr[len(unsortedArr)-1])
  print("partitioned" + str(unsortedArr))
  return i + 1


  


  


  
    
  

  



partitionArr = partition(unsortedArr, len(unsortedArr) - 1)
print(partitionArr)
