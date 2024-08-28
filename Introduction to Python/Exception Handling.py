#try:
    # Code that might raise an exception
    #risky_code()
#except SomeException as e:
    # Code that runs if an exception occurs
    #handle_exception(e)
#else:
    # Code that runs if no exception occurs
    #no_exception_occurred()
#finally:
    # Code that always runs, regardless of exceptions
    #always_run_this()

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    print("No exceptions occurred.")
finally:
    print("This block always executes.")
