import time
def merge_sort(data, left, right, drawrectangle, delay):
    if left < right:
        mid = (left + right) // 2

        # Recursive call on the left and right halves
        merge_sort(data, left, mid, drawrectangle, delay)
        merge_sort(data, mid + 1, right, drawrectangle, delay)

        # Merge the two sorted halves
        merge(data, left, mid, right, drawrectangle, delay)
def merge(data, left, mid, right, drawrectangle, delay):
    left_half = data[left:mid + 1]
    right_half = data[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            data[k] = left_half[i]
            i += 1
        else:
            data[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        data[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        data[k] = right_half[j]
        j += 1
        k += 1

    drawrectangle(data, ['blue' if left <= x <= right else 'red' for x in range(len(data))] )
    time.sleep(delay)
