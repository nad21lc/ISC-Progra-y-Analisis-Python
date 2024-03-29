def computepay(hrs, rate):
    if hrs < 40:
        pay = hrs * rate
    else:
        pay = 40 * rate
        extra = (hrs-40)*rate*1.5
        pay += extra
    return pay


hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter rate: ")
rate = float(rate)

print("Pay",computepay(hrs,rate))