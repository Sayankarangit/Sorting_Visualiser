import time
def heap_sort(data, drawrectangle, delay):
    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] > data[largest]:
            largest = left

        if right < n and data[right] > data[largest]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            drawrectangle(data, ['blue' if x == i or x == largest else 'red' for x in range(len(data))])
            time.sleep(delay)
            heapify(data, n, largest)

    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawrectangle(data, ['blue' if x == 0 or x == i else 'grey' for x in range(len(data))])
        time.sleep(delay)
        heapify(data, i, 0)

    drawrectangle(data, ['green' for x in range(len(data))])
