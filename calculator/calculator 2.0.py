# 🔢 Hello My name is Dev Aka Mama wawa, Here is a calculator for Our son Wawa! 🔢

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("🚫 Please enter a valid number.")

print("🎉 Welcome to the Simple Python Calculator 🎉\n")

# Step 1: Input numbers
num1 = get_number("👉 Enter the first number: ")
num2 = get_number("👉 Enter the second number: ")

# Step 2: Do the math
sum_result = num1 + num2                          # ➕ Addition
difference_result = num1 - num2                   # ➖ Subtraction
product_result = num1 * num2                      # ✖ Multiplication
quotient_result = num1 / num2 if num2 != 0 else "❌ Undefined (cannot divide by zero)"

# Step 3: Display results
print("\n🧮 Calculation Results:")
print(f"🔹 Sum: {num1} + {num2} = {sum_result}")
print(f"🔹 Difference: {num1} - {num2} = {difference_result}")
print(f"🔹 Product: {num1} * {num2} = {product_result}")
print(f"🔹 Quotient: {num1} ÷ {num2} = {quotient_result}")

print("\n✅ All done! Math is fun, right? 😄")