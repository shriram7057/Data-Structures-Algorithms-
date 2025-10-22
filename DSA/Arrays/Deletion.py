#python Program to delete the value using delete operation

if __name__ == '__main__':
    LA = [10, 20, 30, 40, 50]

    print("Array Before Deletion:", LA)
    for x in range(len(LA)):
        print("LA[", x, "] =", LA[x])

    # Element to delete
    element = 60
    print("\nDeleting element:", element)

    if element in LA:
        LA.remove(element)  # remove the element from the list
    else:
        print("Error: Element does not exist in the list")

    print("\nArray After Deletion:")
    for x in range(len(LA)):
        print("LA[", x, "] =", LA[x])


# 1. Start
# 2. Set J = K
# 3. Repeat steps 4 and 5 while J < N
# 4. Set LA[J] = LA[J + 1]
# 5. Set J = J+1
# 6. Set N = N-1
# 7. Stop