"""Challenge 3 - Binary search on a sorted array."""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main() -> None:
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    try:
        target = int(input("Enter the target element: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    print("The array:", arr)
    index = binary_search(arr, target)
    if index != -1:
        print(f"Element {target} is found at index {index}.")
    else:
        print(f"Element {target} is not in the array.")


if __name__ == "__main__":
    main()
