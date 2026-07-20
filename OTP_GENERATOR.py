from random import randint
print("\n-----LOGIN-----")

num = int(input("ENTER YOUR MOBILE NO : "))

otp = randint(1000,9999)
print(f"YOUR OTP IS {otp}")

verify_otp = int(input("ENTER THE OTP :"))

if otp == verify_otp:
    print("SUCCESSFULLY LOGIN")
else:
    print("INVAILD OTP")

