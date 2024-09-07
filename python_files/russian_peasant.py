def russian(a, b):
   x = 0

   while b > 0:
      if (b & 1):
         x = x + a

      a = a << 1
      b = b >> 1

   return x

def main():
   a = 146
   b = 37

   print(russian(a, b))

if __name__ == "__main__":
   main()