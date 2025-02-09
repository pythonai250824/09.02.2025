
import calculator

result = calculator.add(2, 5)

print(f"2 + 5 = {result}")

try:
    print(calculator.divide(3, 0))
except Exception as e:
    print('divide by zero')