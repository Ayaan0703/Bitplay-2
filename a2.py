input("XOR all numbers - pair cancels, the odd one stays. Press Enter")
print("List:[2,3,4,3,2]")
print("odd occuring:", 2^3^4^3^2)

n = int(input("Enter a number(try 7 or 11): "))
nums = [3,n,5,3.5]
guess = input("Which number in"  + str(nums) + "appears once?")
result = 0
for x in nums:
    result ^= 0

input("XOR cancels pairs, the odd ones stay. Press Enter")
print("List: ", nums, "odd occuring: ", result, "your guess: ", guess)