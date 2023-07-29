
def reverse(arr, start, end):
    if start>=end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr, start+1, end-1)


if __name__ == "__main__":
    arr = [10,20,45,21,93,85,65]
    start = 0
    end = len(arr)-1

    print(arr)

    reverse(arr, start, end)

    print(arr)