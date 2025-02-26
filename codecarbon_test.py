from codecarbon import EmissionsTracker

# Initialize the tracker
tracker = EmissionsTracker(measure_power_secs=0.1)

# Start tracking energy usage
tracker.start()

# Example function to measure energy usage
# def fib(n):
#     my_list = [1, 1]
#     for i in range(n):
#         my_list.append(my_list[-1] + my_list[-2])
#     return my_list[-1]
#

#0, 1, 2, 3, 4, 5, 6
#1, 1, 2, 3, 5, 8, 13
def fib(n):
  if n <= 1:
    return 1
  
  first, second = 1, 1
  result = 0
  for i in range(2, n+1):
    result = first + second
    first, second = second, result
  
  return result
    


result = 0
# Call the function
for i in range(1, 10):
    result = fib(10000)

# Stop tracking energy usage
tracker.stop()

# print(f"Fibonacci result: {result}")