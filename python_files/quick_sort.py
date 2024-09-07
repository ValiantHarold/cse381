import random

def quick_sort(list):
   # escape clause
   if len(list) <= 1:
      return list
   
   # set variables
   pivot = list[0]
   smaller = []
   larger = []

   # check every value past 1 this will exclude 0
   for i in list[1:]:
      if i < pivot:
         smaller.append(i)
      else:
         larger.append(i)

   smaller_final = quick_sort(smaller)
   larger_final = quick_sort(larger)
   list_final = smaller_final + [pivot] + larger_final
   
   return list_final

def main():
   my_list = random.sample(range(1, 50), 10)
   print(f'Before sorting:  {my_list}')
   
   my_list = quick_sort(my_list)

   print(f'After sorting: {my_list}')

if __name__ == "__main__":
   main()