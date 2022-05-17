# TODO здесь писать код
year_start = 1900
year_stop = 2000

for year in range(year_start, year_stop+1):
  for number in range(10):
    count = 0
    for num in str(year):
      if int(num) == int(number):
        count += 1
      if count >= 3:
        print(year)