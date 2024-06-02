def add(num1, num2):
    ans = num1 + num2
    return ans

def sub(num1, num2):
    ans = num1 - num2
    return ans

def mul(num1, num2):
    ans = num1 * num2
    return ans

def div(num1, num2):
    ans = num1 / num2
    return ans


a = 100
b = 20
ans = add(a,b)
print(f"Addition of {a} and {b} is {ans}")

ans = sub(a,b)
print(f"Subtraction of {a} and {b} is {ans}")

ans = mul(a,b)
print(f"Multiplication of {a} and {b} is {ans}")

ans = div(a,b)
print(f"Division of {a} and {b} is {ans}")