import random

def _merge_sort(left_list, right_list):
   result_list = []
   i = 0
   j = 0

   while i < len(left_list) and j < len(right_list):
      # Add the smaller of the two lists to the result list
      if left_list[i] < right_list[j]:
         result_list.append(left_list[i])
         i += 1
      else:
         result_list.append(right_list[j])
         j += 1

   result_list += left_list[i:]
   result_list += right_list[j:]

   print(f'During sorting: {result_list}')

   return result_list

def merge_sort(list):
   # escape clause
   if len(list) <= 1:
      return list

   # set variables
   mid = len(list) // 2
   left_list = list[:mid]
   right_list = list[mid:]
    
   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
    
   return _merge_sort(left_list, right_list)

def main():
   my_list = random.sample(range(1, 50), 10)
   print(f'Before sorting:  {my_list}')
   
   my_list = merge_sort(my_list)

   print(f'After sorting: {my_list}')

if __name__ == "__main__":
   main()