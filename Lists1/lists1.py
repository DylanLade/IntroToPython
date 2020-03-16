# arrays1 assignment by Dylan Lade for Python Programming 1

def display_list(label, items):
    print(label)
    for item in items:
        print(item)

foods = ["pizza", "salad", "hamburger", "steak", "apple", "orange"]

def main():
# Display the original array 
    display_list("foods in origional order: ", foods)
# Display the sorted array   
    foods.sort()
    display_list("foods in ascending alphabetical order: ", foods)
# Display the reverse sorted array    
    foods.sort(reverse=True)
    display_list("foods in descending alphabetical order: ", foods)
# Copy the orignal array and sort the copy
    foods2 = foods.copy()
    foods2.sort()
    display_list("foods2 in ascending alphabetical order: ", foods2)
# Show the original array still in reverse order
    display_list("foods still in descending alphabetical order: ", foods)
# Reverse the decending array to make it sorted
    foods.reverse()
    display_list("foods in ascending alphabetical order: ", foods)
# Append the new items to the sorted array
    foods.append("carrots")
    foods.append("milk")
    display_list("sorted foods with carrots and milk appended to end: ", foods)
# Sort the array with the new items 
    foods.sort()
    display_list("foods in ascending alphabetical order: ", foods)
# Find the index of pizza
    pizza_index = foods.index("pizza")
    print("Pizza is at " + str(pizza_index))
# Insert fries into the index of pizza and find new pizza index
    foods.insert(pizza_index, "fries")
    pizza_index = foods.index("pizza")
    print("Pizza is now at " + str(pizza_index))

if __name__ == "__main__":
    main()

    



