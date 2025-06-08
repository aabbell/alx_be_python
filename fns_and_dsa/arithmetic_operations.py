def perform_operation(num1 ,num2 ,operation):
    if operation == add:
        print(f"Result: {num1 + num2}")
    elif operation == substract:
        print(f"Result: {num1 - num2}")
    elif operation == multiply:
        print(f"Result: {num1 * num2}")
    elif operation == divide:
        if num2 == 0:
            print("num2 can't be 0")
        print(f"Result: {num1 / num2}")
        