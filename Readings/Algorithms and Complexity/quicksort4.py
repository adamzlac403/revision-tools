array = [20,90,40,80,30,60,100,10,70,50]
def quickSort(array, p, r):
  if (p<r):
    print("iteration with values array" + str(array) + "p" + str(p))
    q = partition(array,p,r)
    quickSort(array, p ,q - 1)
    quickSort(array, q + 1, r)

def partition(array, p ,r):
  x = array[r]
  i = p - 1
  for j in range(p, r):
    if array[j] <= x:
      i = i + 1
      array[j], array[i] = array[i],array[j]
  array[i+1],array[r] = array[r],array[i+1]
  print(array)
  return i+1

quickSort(array,0, len(array)-1)