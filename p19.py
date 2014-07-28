


def ndays(year,month):
   monthlengths = { 1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   if month == 2:
      if not year % 400:
         return 29
      elif not year % 100:
         return 28
      elif not year % 4:
         return 29
      else:
         return 28
   else:
      return monthlengths[month]
      

days = 1
nsundays = 0
for year in range(1900,2001):
   for month in range(1,13):
      days += ndays(year,month)
      if year > 1900:
         if not days % 7:
            nsundays +=1
         

print nsundays
