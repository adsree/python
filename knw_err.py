import sys

num= int(input("Enter numerator"))
den= int(input("Enter denominator"))
try:
    res=num/den
    print (res)
except:
    print("Exception handled")
    print("oops!",sys.exc_info()[0],"occured")

print("End of prgrm")