# math module examples
import math

num1 = math.sqrt(144)
print("num1: ", num1)

num2 = math.pow(2,5)
print("num2: ", num2)


num = 4250000
div = 10 ** len(str(num-1))
digit = num // div
remainder = num % div

print("num: ", num)
print("div: ", div)
print("digit: ", digit)
print("remainder: ", remainder)