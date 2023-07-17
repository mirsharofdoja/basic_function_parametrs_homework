# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average(list):
    average=0
    for i in list:
        average+=i
    return average/len(list)