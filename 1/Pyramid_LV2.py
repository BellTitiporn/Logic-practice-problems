#Question form Borntodev LAB

#Create Pyramid Level1

# Example

# Input Int = 3

# Output =>         *
#                  ***
#                 *****

#############################################################


def create_christmas_tree(height):
    for row in range(1, height + 1):
        spaces = height - row
        print(' ' * spaces + '*' * (2 * row - 1))

# Example usage
height_input = int(input())
create_christmas_tree(height_input)