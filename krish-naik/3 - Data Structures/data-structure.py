list_names = ["Praveen", "Krish", "Anil", 1, 2, 3, True, "Python"]
print(f"list with mixed data types: {type(list_names)}")
print(list_names[0])
print(list_names[-1])
list_names.append("Javascript")
print(list_names)

for index, item in enumerate(list_names):
    print(index, item)

print("list comprehension")

num_squares = [i**2 for i in range(10)]
print(num_squares)
even_numbers = [num for num in range(10) if num % 2 == 0]
print(f"even numbers: {even_numbers}")
