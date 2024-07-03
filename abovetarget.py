def aboveTarget(values, target):
    for value in values:
        if value > target:
            return True
    return False

# Test the function with the provided example
x = [3, 4, 5, 6, 7, 8]
print(aboveTarget(x, 7))  # Output: True
