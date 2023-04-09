import string
import random

length = 19
amount_of_codes = int(input("How many codes do you need? "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

combined = lower + upper + num

for i in range(amount_of_codes):
  temp = random.sample(combined,length)
  code = "".join(temp)
  print(code)
