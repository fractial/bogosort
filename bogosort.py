import random

def is_sorted(arr):
  for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
      return False
    return True

def bogosort(arr):
  while not is_sorted(arr):
    print(arr)
    random.shuffle(arr)
  return arr

if __name__ == '__main__':
  numbers = input('Enter your numbers seperated by spaces: ').split()
  unsorted_arr = [int(num) for num in numbers]
  print("Unsorted array:", unsorted_arr)
  sorted_arr = bogosort(unsorted_arr)
  print("Sorted array:", sorted_arr)
