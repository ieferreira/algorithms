def binary_search(ls, low, high, x):

    if high >= low:
        mid = (high + low) // 2

        if ls[mid] == x:
            return mid

        elif ls[mid] > x:
            return binary_search(ls, low, mid - 1, x)

        else:
            return binary_search(ls, mid + 1, high, x)

    else:
        return None


ls = [2, 3, 4, 10, 14, 21, 25, 29, 32, 220, 980, 1001, 1200, 1230]
x = 1001

result = binary_search(ls, 0, len(ls)-1, x)

if result is not None:
    print(f"Element {x} is  present at index {result}")
else:
    print(f"Element {x} not found")
