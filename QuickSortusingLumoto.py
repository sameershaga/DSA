'''
Quick sort with Lomuto's partitioning (idea explained in Levitin's Chapter 4)
Dr. Olcay Kursun, Data Structures&Algorithms, Fall 2022, AUM Computer Science
'''

def lomuto(a, left, right):
  pivot_val = a[left]
  s = left
  i = left + 1
  while i < right and a[i] <= pivot_val:
    i += 1
    s += 1
  while i < right:
    if a[i] > pivot_val:
      i += 1
    else:
      s += 1
      temp = a[s]
      a[s] = a[i]
      a[i] = temp
      i += 1
  a[left] = a[s]
  a[s] = pivot_val
  return s

def quicksort(a, left = 0, right = None):
  if right is None:
    right = len(a)
  if left + 1 >= right:
    return
  k = lomuto(a, left, right)
  quicksort(a, left, k)
  quicksort(a, k+1, right)

if __name__ == '__main__':
  import random
  unsorted_list = [random.randint(0,10000) for i in range(500)]
  mysorted_list = unsorted_list.copy()
  quicksort(mysorted_list)
  print(mysorted_list == sorted(unsorted_list))
