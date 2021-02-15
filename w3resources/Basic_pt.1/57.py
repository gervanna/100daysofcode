#Write a program to get execution time for a Python method.

#02_13_21

import time

start_time = time.time()

end_time = time.time()

print(f"Time passed: {end_time - start_time}")


def timetaken(func, *args, **kwargs):
    # func is whatever function we want to time

    start = time.time() # start the timer

    result = func(*args, **kwargs) # run the function with whatever arguments we got

    end = time.time() # stop the timer

    print(f"time elapsed: {end - start} seconds") # print the time taken

    return result # return the answer to the function.


print("\nTime taken\n")
print(f"sum result: {timetaken(sum, range(10000000))}\n") # time how long it will take to sum 10 million integers
