from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry("750x600")
root.config(bg='Yellow')

select_algorithm = StringVar()
arr = []


# GENERATING THE ARRAY
def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())

    arr = []
    for i in range(size):
        arr.append(random.randrange(lowest, highest + 1))

    drawrectangle(arr, ['red' for x in range(len(arr))])


# DRAWING THE ARRAY ELEMENTS AS RECTANGLES
def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        # top left coordinates
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        # bottom right coordinates
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(arr[i]))

    root.update_idletasks()


def sorting():
    global arr
    selected_algorithm = select_algorithm.get()
    if selected_algorithm == 'Bubble Sort':
        bubble_sort(arr, drawrectangle, sortingspeed.get())
    elif selected_algorithm == 'Merge Sort':
        merge_sort(arr, 0, len(arr) - 1, drawrectangle, sortingspeed.get())
    elif selected_algorithm == 'Heap Sort':
        heap_sort(arr, drawrectangle, sortingspeed.get())
    elif selected_algorithm == 'Quick Sort':
        quick_sort(arr, 0, len(arr) - 1, drawrectangle, sortingspeed.get())
    elif selected_algorithm == 'Insertion Sort':
        insertion_sort(arr, drawrectangle, sortingspeed.get())
    drawrectangle(arr, ['green' for x in range(len(arr))])




# GUI CODING PART

options_frame = Frame(root, width=700, height=300, bg='green')
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=350, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(options_frame, text="Algorithm Choice: ", ).grid(row=0, column=0, padx=10, pady=10)

algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Bubble Sort','Insertion Sort', 'Merge Sort', 'Heap Sort', 'Quick Sort'], width=10)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.09, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL,
                     label="Sorting Speed ")
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

Button(options_frame, text="Start Sorting", command=sorting, bg='silver', height=5).grid(row=0, column=3, padx=5, pady=5)

lowest_Entry = Scale(options_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=1, to=30, resolution=1, orient=HORIZONTAL, label="Array size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(options_frame, text="Current Array", command=Generate_array, bg='silver', height=5).grid(row=1, column=3, padx=10,
                                                                                              pady=10)

root.mainloop()
