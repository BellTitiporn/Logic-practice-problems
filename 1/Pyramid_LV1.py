#Question form Borntodev LAB

#Create Pyramid Level1

# Example

# Input Int = 4

# Output =>     *
#               **
#               ***
#               ****

#############################################################

n = int(input())  
for i in range(0, n):  

        for j in range(0, i + 1):  
          
            print("*", end="")       
  
        print()  