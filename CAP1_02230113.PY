################################
# Tshering Wangda
# First Year ECE
# 02230113
################################
# REFERENCES
################################
# SOLUTION
# Total Score:
# 
################################

def read_input(file_path):
# read the contents of a file located at the specified file_path. 
    with open(file_path, 'r') as file: # opens the file specified by file_path in read mode ('r'). 
        content = file.read() # reads the entire contents of the file and stores it in the variable content as a single string.
        lines = content.strip().split('\n') 
# removes any leading or trailing whitespace from the content string using strip() and then splits the string into a list of lines based on the newline character '\n'.      
        rounds = [line.strip().split() for line in lines]
# line creates a list called rounds using a list comprehension. It iterates over each line in the lines list, removes leading and trailing whitespace using strip(), and then splits each line into a list of words using split()
    return rounds

def calculate_score(rounds): # Define the fuction to calculate the scores
    total_score = 0 # Initialize the total score to zero
    for shape, outcome in rounds: # Iterate over each lines in the list
    # Check if the shape is A and the outcome is X
        if shape == "A" and outcome == "X":
        # Add 3 to the total score
            total_score += 3
    # Check if the shape is A and the outcome is Y
        elif shape == "A" and outcome == "Y":
            # Add 4 to the total score
            total_score += 4
    # Check if the shape is A and the outcome is Z
        elif shape == "A" and outcome == "Z":
            # Add 8 to the total score
            total_score += 8
    # Check if the shape is B and the outcome is X
        elif shape == "B" and outcome == "X":
            # Add 1 to the total score
            total_score += 1
    # Check if the shape is B and the outcome is Y
        elif shape == "B" and outcome == "Y":
            # Add 5 to the total score
            total_score += 5
    # Check if the shape is "B" and the outcome is Z
        elif shape == "B" and outcome == "Z":
            # Add 9 to the total score
            total_score += 9
    # Check if the shape is "C" and the outcome is X
        elif shape == "C" and outcome == "X":
            # Add 2 to the total score
            total_score += 2
    # Check if the shape is C and the outcome is Y
        elif shape == "C" and outcome == "Y":
            # Add 6 to the total score
            total_score += 6
    # Check if the shape is C and the outcome is Z
        elif shape == "C" and outcome == "Z":
            # Add 7 to the total score
            total_score += 7
        else:
            # If the shape and outcome combination is not recognized or accept, print("Invalid!")
            print("Invalid!")
            # Return 0 to indicate an error
            return 0
        # Return the total score after all rounds have been processed
    return total_score

# Define the name of the input file 
file_path = "input_3_cap1.txt"
# Read the data from the file and return it in a suitable format
rounds = read_input(file_path)
# Calculate the total score based on the "rounds" data.
total_score = calculate_score(rounds)
# Display the total score in a readable format.
print(f"The total score is: {total_score}")