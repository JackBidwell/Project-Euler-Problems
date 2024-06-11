series = 0

for value in range(1, 1001):
  series = series + (value**value)

series = str(series)
series = series[-10: -1]
series = int(series)
print(series)
