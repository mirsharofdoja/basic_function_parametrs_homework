# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min