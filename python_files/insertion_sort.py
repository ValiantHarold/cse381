import random

def insertion_sort(list):

   for i in range(1, len(list)):
      key = list[i]
      j = i - 1

      while j >= 0 and list[j] > key:
         list[j + 1] = list[j]
         j -= 1
      list[j + 1] = key
      
      print(f'During sorting: {list}')

def main():
   my_list = random.sample(range(1, 50), 10)
   print(f'Before sorting:  {my_list}')
   
   insertion_sort(my_list)

   print(f'After sorting: {my_list}')

if __name__ == "__main__":
   main()