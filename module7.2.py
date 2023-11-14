S = 'mumbai'

# Print each character and its Unicode code point using a for loop
for i in S:
    code_point = ord(i)
    print(f"Character: {i}, Unicode Code Point: {code_point}")

# Compute the sum of Unicode code points using a for loop
total_code_points = 0
for i in S:
    total_code_points += ord(i)
print(f"Sum of Unicode code points:", total_code_points)

# Return a list containing Unicode code points using map class
code_points_map_class = list(map(ord, S))
print(f"Unicode code points using map class:", code_points_map_class)
