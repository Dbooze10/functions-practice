def hello():
    print("Hello user")

def pack(arg_1, arg_2, arg_3):
   return[arg_1, arg_2, arg_3]

def eat_lunch(meal):
  if len(meal) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(meal)):
      if i == 0:
        print(f"First I eat {meal[0]}")
      else:
        print(f"Next I eat {meal[i]}")

hello()
print(pack("a","b","c"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
