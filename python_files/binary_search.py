import random

def binary_search(list, target):
   low = 0
   high = len(list) - 1
   x = 0

   while low <= high:
      x += 1
      mid = (low + high) // 2
      
      if low > high:
         print(f'Number {target} is not found in list')
         break
      elif list[mid] < target:
         low = mid + 1
      elif list[mid] > target:
         high = mid - 1
      else:
         print(f'Number {target} found in {x} tries!')
         break

def main():
   my_list = random.sample(range(1, 50), 10)
   my_list.sort()

   print(f'Your list is {my_list}')
   num = int(input('Enter a number: '))
   
   binary_search(my_list, num)

if __name__ == "__main__":
   main()