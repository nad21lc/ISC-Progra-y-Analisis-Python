hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter rate: ")
rate = float(rate)

if hrs < 40:
    pay = hrs * rate
else:
    pay = 40 * rate
    extra = (hrs-40)*rate*1.5
    pay += extra
    
print(pay)