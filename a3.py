input("XOR all - pairs cancel, two odd-occuring ones remain. Press Enter")
print("[1,4,3,3] XOR of all:", 1^4^3^3, "binary: ", bin(1^4^3^3)[2:])
print("Split bit 1 -> group A (bit 0 on): 1   group B (bit 0 off): 4")

n = int(input("enter a number (try 6 or 9):"))
guess = input("is bit 0 of" + str(n)+ "ON (yes/no)?")
input("check the split bit. Press Enter:")
if n & 1:
    print("", n, "binary", bin(n)[2:],"bit 0 on - group A your guess", guess)
else:
    print("", n, "binary", bin(n)[2:],"bit 0 off - group B your guess", guess)