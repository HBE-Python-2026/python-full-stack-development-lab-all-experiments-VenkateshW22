# Experiment 3: Functions and Exception Handling

def safe_divide(numerator, denominator):
    try:
        # TODO: Perform the division: result = numerator / denominator
        # TODO: Return the result
        pass
    except ZeroDivisionError:
        # TODO: Print "Error: Cannot divide by zero."
        # TODO: Return None
        pass
    except TypeError:
        # TODO: Print "Error: Inputs must be numbers."
        # TODO: Return None
        pass

def main():
    print("--- Testing safe_divide ---")
    # Test cases (Do not change these)
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"'ten'/ 2 = {safe_divide('ten', 2)}")

if __name__ == "__main__":
    main()