array = [20,90,50,80,30,100,10,70,40]

def quicksort(array,startPoint,pivot):
  while(startPoint < pivot):
    q = partition(array,startPoint,pivot)
    quicksort(array,startPoint,pivot-1)
    quicksort(array,pivot-1, startPoint)
    
def partition(array,startPoint,pivot):
  print("Partition called with array "+ str(array))
  pivotValue = array[pivot]
  newStartPoint  = startPoint - 1
  for startPoint in range(pivot):
    print("startPoint value = " + str(array[startPoint]) + " array = " + str(array))
    if array[startPoint] < pivotValue:
      newStartPoint +=1
      print("value at nSP " + str(array[newStartPoint]) + " index " + str(newStartPoint))
      array[startPoint],array[newStartPoint] = array[newStartPoint],array[startPoint]
      startPoint+=1
    if array[startPoint] > pivotValue: startPoint+=1
  
  array[newStartPoint+1], array[startPoint] = array[startPoint], array[newStartPoint+1]
  print("array =" + str(array) + "i= " + str(newStartPoint+1))
  return newStartPoint + 1


print("First run")
i = partition(array, 0, len(array)-1)
print("2nd Runs ")
print("action on the less than section")
quicksort(array, 0, len(array)-1)
      

  