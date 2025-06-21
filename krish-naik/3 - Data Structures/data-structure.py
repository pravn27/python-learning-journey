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

# Given a list with duplicates, remove duplicates using set
nums = [1, 2, 2, 3, 4, 4, 5]
print(f"unique elements: {set(nums)}")

# Use set intersection
list1 = [1, 2, 3]
list2 = [3, 4, 5]
common_elements = set(list1).intersection(set(list2))
print(f"common elements: {common_elements}")

# Hint: split sentence into words and use set
sentence = "the quick brown fox jumps over the lazy dog the quick fox"
unique_words = set(sentence.split())
print(f"unique words: {unique_words}")
print(f"number of unique words: {len(unique_words)}")
