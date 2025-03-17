# Example program to demonstrate debugging techniques

# Conditional breakpoint: Stop when variable x equals 10
for x in range(15):
      # You can set a conditional breakpoint here.
     print(f"Stopping because x is {x}")
       

# Loop counter breakpoint: Stop on the last iteration
counter = 0
for i in range(5):  # Expected loop to run 5 times
    counter += 1
    
    print(f"Stopping on the last iteration: counter = {counter}")

# Logging variable changes inside a loop
for num in range(5):
    updated_value = num * 2  # Variable changes here
    print(f"Logging updated_value: {updated_value}")  # Add a log point here
