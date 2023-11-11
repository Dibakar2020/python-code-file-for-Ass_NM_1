for divisor in range(6):
    try:
        result = 1 / divisor
        print(f"1 divided by {divisor} is {result}")
    except ZeroDivisionError:
        print(f"1 divided by {divisor} is indeterminate")
