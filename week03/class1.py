import random
LIST_SIZE = 10
NUMBER_LOW = 0
NUMBER_HIGH = 15

nlist = [random.randint(NUMBER_LOW, NUMBER_HIGH) for _ in range(LIST_SIZE)]
nlist.sort()

n = 3
low = 0
mid = 0
high = LIST_SIZE
x = 0

print(nlist)
print(f'Your number is {n}')
print()

while low <= high:
    x += 1
    mid = (high + low) // 2

    print(f'Your choice is {nlist[mid]}')

    if nlist[mid] < n:
        low = mid + 1

    elif nlist[mid] > n:
        high = mid - 1

    else:
        print(f'Number {n} found in {x} tries!')
        break

    if low > high:
        print(f'Number {n} is not found in list')

    

