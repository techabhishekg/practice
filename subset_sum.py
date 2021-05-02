def sumSubsets(sets, n, target):
    # Create the new array with size
    # equal to array set[] to create
    # binary array as per n(decimal number)
    x = [0] * len(sets);
    j = len(sets) - 1;

    # Convert the array into binary array
    while (n > 0):
        x[j] = n % 2;
        n = n // 2;
        j -= 1;

    sum = 0;

    # Calculate the sum of this subset
    for i in range(len(sets)):
        if (x[i] == 1):
            sum += sets[i];

    # Check whether sum is equal to target
    # if it is equal, then print the subset
    if (sum == target):
        import pdb; pdb.set_trace()

        print("{", end=" ");
        for i in range(len(sets)):
            if (x[i] == 1):
                print(sets[i], end=", ");
        print("}, ", end=" ");

    # Function to find the subsets with sum K


def findSubsets(arr, K):
    # Calculate the total no. of subsets
    x = pow(2, len(arr));

    # Run loop till total no. of subsets
    # and call the function for each subset
    for i in range(1, x):
        sumSubsets(arr, i, K);

    # Driver code


if __name__ == "__main__":
    arr = [5, 10, 12, 13, 15, 18];
    K = 30;
    findSubsets(arr, K);