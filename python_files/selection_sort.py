import random

def selection_sort(list):
   for i in range(len(list)):
      min_idx = i
      for j in range(i + 1, len(list)):
         if list[j] < list[min_idx]:
            min_idx = j
      list[i], list[min_idx] = list[min_idx], list[i]
      print(f'During sorting: {list}')
   return list

def main():
   my_list = random.sample(range(1, 50), 10)
   print(f'Before sorting: {my_list}')
   
   selection_sort(my_list)

   print(f'After sorting:  {my_list}')

if __name__ == "__main__":
   main()
