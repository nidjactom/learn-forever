##def computepay(h,r):
##    if h > 40:
##        pay = (40 * r) + ((h-40) * r * 1.5)
##    else:
##        pay = h * r
##    return pay
##
##hrs = input("Enter Hours:")
##rate = input("Enter rate:")
##h=float(hrs)
##r=float(rate)
##p = computepay(h,r)
##print(p)

largest = None
smallest = None
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        number = int(num)
    except:
        print('Invalid input')
    if largest is None:
        largest = number
    elif number > largest:
        largest = number
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
print('Maximum is', largest)
print('minimum is', smallest)
        
