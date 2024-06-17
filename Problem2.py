length = input("What is the highest number of Fibanicci you would like to calculate: ")

length = int(length)
fibonacci = [1]
num = 0
sum = 0
i = 0
while i < length:
  num = num + fibonacci[i - 1]
  if num % 2 == 0:
    fibonacci.append(num)
    sum += num
  i += 1

print(sum)


