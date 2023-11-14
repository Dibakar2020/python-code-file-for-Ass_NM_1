# List comprehension methods
S = 'mumbai'

# Print each character in the string and its Unicode code point
for i in S:
    code_point = ord(i)
    print(f"Character: {i}, Unicode Code Point: {code_point}")

# Compute the sum of Unicode code points
total_code_points = sum(ord(i) for i in S)
print(f"Sum of Unicode code points:", total_code_points)

# Return a list containing Unicode code points using list comprehension
code_points_list_comprehension = [ord(i) for i in S]
print(f"Unicode code points using list comprehension:", code_points_list_comprehension)
