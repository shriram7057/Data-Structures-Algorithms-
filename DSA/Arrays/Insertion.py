# 1. Start
# 2. Create an Array of a desired datatype and size.
# 3. Initialize a variable 'i' as 0.
# 4. Enter the element at ith index of the array.
# 5. Increment i by 1.
# 6. Repeat Steps 4 & 5 until the end of the array.
# 7. Stop
def insert(arr, element):
    arr.append(element)

if __name__ == "__main__":
    LA = [10, 20, 30, 40, 50]

    # Array Before inserting an element
    print("Array Before Insertion:", LA)
    for x in range(len(LA)):                # Loop tp print each element in the array
        print("LA[", x, "] =", LA[x])

    print("\nInserting element.....")
    insert(LA, 60)  # inserting new element

    # Array after inserting an element
    print("\nArray After Insertion:")
    for x in range(len(LA)):
        print("LA[", x, "] =", LA[x])
