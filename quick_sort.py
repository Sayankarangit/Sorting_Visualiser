import time

def quick_sort(data, low, high, drawrectangle, delay):
    if low < high:
        partition_index = partition(data, low, high, drawrectangle, delay)
        quick_sort(data, low, partition_index - 1, drawrectangle, delay)
        quick_sort(data, partition_index + 1, high, drawrectangle, delay)

def partition(data, low, high, drawrectangle, delay):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            drawrectangle(data, ['blue' if x == i or x == j else 'red' for x in range(len(data))] )
            time.sleep(delay)

    data[i + 1], data[high] = data[high], data[i + 1]
    drawrectangle(data, ['blue' if x == i + 1 or x == high else 'red' for x in range(len(data))] )
    time.sleep(delay)

    return i + 1
