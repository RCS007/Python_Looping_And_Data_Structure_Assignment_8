# Question 8:

# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is
# string, age and height are numbers. The tuples are input by console.

# The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.

# The priority is that name > age > score.

# If the following tuples are given as input to the program:

#Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85

# Then, the output of the program should be:

# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21',
# '85'), ('Tom', '19', '80')]


# Function to sort tuples based on name, then age, then height
def sort_tuples(tuples_list):
    # Sort by name first, then age, then height
    return sorted(tuples_list, key=lambda x: (x[0], int(x[1]), int(x[2])))

# Input the tuples from the user
tuples = []
n = int(input("Enter the number of tuples: "))
for _ in range(n):
    name, age, height = input("Enter name, age, height separated by commas: ").split(',')
    tuples.append((name, age, height))

# Sort the tuples using the defined function
sorted_tuples = sort_tuples(tuples)

# Print the sorted tuples
print(sorted_tuples)
