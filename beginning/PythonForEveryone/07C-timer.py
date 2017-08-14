import time

input("Enter and count to 20.")
start = time.time()

input("After 20 seconds, enter.")
end = time.time()

et = end - start
print("Time elapsed: ", et, "seconds")
print("Difference: ", abs(et - 20), "seconds")
