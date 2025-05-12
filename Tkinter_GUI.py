#!/usr/bin/env python

# zFa3 - Tkinter_Sorting
# Tkinter Sorting Animations
import tkinter as tk, random as rd, time as tm, tkinter.messagebox

tkinter.messagebox.showinfo("Keybinds", """
        r --> radix Sort\n
        c --> comb Sort\n
        b --> bubble sort\n
        m --> merge sort\n
        space --> randomize array\n
        o --> odd even sort\n
        s --> shaker sort\n
        C --> randomize color\n
        """)

SCREEN_WID = 600
ELEMENTS_TO_SORT = 50
PADDING = 20
PADDING = 0
HEIGHT = 0
COMB_SORT_SHRINK_FACTOR = 13
RANDOMIZER = ELEMENTS_TO_SORT * 2
VALUE_MULTIPLIER = (SCREEN_WID - PADDING * 2)//ELEMENTS_TO_SORT
STATIC_COLOR = (255, 50, 10)
DELAY = 100
DELAY = 0

elements = [abs(counter1 - ELEMENTS_TO_SORT) for counter1 in range(ELEMENTS_TO_SORT)]
ELEM_WID = (SCREEN_WID - PADDING * 2)//ELEMENTS_TO_SORT
SIDE_PADDING = int(ELEM_WID * 0.01)
ELEMENTS_TO_SORT = min(SCREEN_WID - PADDING * 2, ELEMENTS_TO_SORT)

root = tk.Tk()
root.geometry(f"{SCREEN_WID}x{SCREEN_WID}")
root.title("Sorting Algorithms")
canvas = tk.Canvas(root, width = int(SCREEN_WID), height = int(SCREEN_WID))

def shuffle(elements: list):
        new_lst = elements[:]
        for _ in range(RANDOMIZER):
            a, b = rd.randint(0, len(elements) - 1), rd.randint(0, len(elements) - 1)
            new_lst[a], new_lst[b] = new_lst[b], new_lst[a]
        return new_lst

elements = shuffle(elements)


def set_elements(list: list):
    global elements
    elements = list[:]

def main():
    global elements

    def randomize(e):
        global elements
        elements = shuffle(elements)
        draw(elements)

    def add_tups(tup: tuple):
        return tuple(map(lambda x, y: min(x + y, 255), STATIC_COLOR, tup))

    def draw_elem(item):
        canvas.create_line(item[0][1], item[0][0], item[0][1], item[0][0] - item[1], width=ELEM_WID - SIDE_PADDING, fill=f"{rgb_to_hex((add_tups((int(item[2]/ELEMENTS_TO_SORT * 255), int(item[2]/ELEMENTS_TO_SORT * 255), int(item[2]/ELEMENTS_TO_SORT * 255)))))}")

    def rand_col(event):
        global STATIC_COLOR
        #STATIC_COLOR = (rd.randint(0, 200),rd.randint(0, 100), rd.randint(150, 250))
        STATIC_COLOR = (rd.randint(0, 255),rd.randint(0, 255), rd.randint(0, 255))
        draw(elements)

    def draw(elements: list):
        canvas.after(DELAY)
        canvas.delete("all")
        for index, item in enumerate(elements):
            draw_elem(((abs(HEIGHT - 600), int(index * int(ELEM_WID) + int(PADDING))), item * VALUE_MULTIPLIER, item))
        canvas.pack()
    
    def inverted(rgb: tuple):
        return (abs(rgb[0] - 255), abs(rgb[1] - 255), abs(rgb[2] - 255))

    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % inverted(rgb)

    def bubble_sort(event):
        time1 = tm.perf_counter()
        list_A = elements[:]
        writes_to_array = 0
        comparisons = 0

        for _ in range(ELEMENTS_TO_SORT):
            for index in range(len(list_A)):
                try:
                    comparisons += 1
                    if list_A[index] > list_A[index + 1]:
                        writes_to_array += 2
                        list_A[index], list_A[index + 1] = list_A[index + 1], list_A[index]
                        draw(list_A)
                        canvas.update()
                except: pass
        draw(list_A)
        canvas.update()
        print(f"DEBUG INFO - Bubble Sort")
        print(f"Time Taken {tm.perf_counter() - time1: 0.2f}s")
        set_elements(list_A)
    
    def odd_even_sort(event):
        time1 = tm.perf_counter()
        list_A = elements[:]
        writes_to_array = 0
        comparisons = 0

        sorted = False
        while not sorted:
            counter1 = 0
            sorted = True
            is_even = 0
            if len(list_A) % 2 == 0:
                is_even = 0
            else:
                is_even = 1
            try:
                for _ in range((len(list_A)//2)+is_even + 1):
                    if list_A[counter1] > list_A[counter1 + 1]:
                        comparisons += 1
                        list_A[counter1], list_A[counter1 + 1] = list_A[counter1 + 1], list_A[counter1]
                        writes_to_array += 2
                        sorted = False
                        draw(list_A)
                        canvas.update()
                    counter1 += 2
            except:
                if is_even == 1:
                    counter1 -= 1
                    if list_A[counter1] > list_A[counter1 + 1]:
                            comparisons += 1
                            list_A[counter1], list_A[counter1 + 1] = list_A[counter1 + 1], list_A[counter1]
                            writes_to_array += 2
                            sorted = False
                            draw(list_A)
                            canvas.update()
            counter1 = len(list_A) - is_even
            try:
                for _ in range((len(list_A)//2)+is_even):
                    counter1 -= 2
                    if counter1 in (-1, 0):
                        counter1 = 1 + is_even
                    if list_A[counter1] < list_A[counter1 - 1]:
                        list_A[counter1], list_A[counter1 - 1] = list_A[counter1 - 1], list_A[counter1]
                        sorted = False
                        draw(list_A)
                        canvas.update()
            except: pass

        draw(list_A)
        canvas.update()
        print(f"DEBUG INFO - Odd Even Sort")
        print(f"Time Taken {tm.perf_counter() - time1: 0.2f}s")
        set_elements(list_A)
    
    def shaker_sort(event):
        time1 = tm.perf_counter()
        list_A = elements[:]
        writes_to_array = 0
        comparisons = 0

        for _ in range(ELEMENTS_TO_SORT//2):
            for index in range(len(list_A)):
                try:
                    comparisons += 1
                    if list_A[index] > list_A[index + 1]:
                        writes_to_array += 2
                        list_A[index], list_A[index + 1] = list_A[index + 1], list_A[index]
                        draw(list_A)
                        canvas.update()
                except: pass
            for index in range(len(list_A)):
                try:
                    comparisons += 1
                    if list_A[abs(index - ELEMENTS_TO_SORT)] > list_A[abs(index - ELEMENTS_TO_SORT) + 1]:
                        writes_to_array += 2
                        list_A[abs(index - ELEMENTS_TO_SORT)], list_A[abs(index - ELEMENTS_TO_SORT) + 1] = list_A[abs(index - ELEMENTS_TO_SORT) + 1], list_A[abs(index - ELEMENTS_TO_SORT)]
                        draw(list_A)
                        canvas.update()
                except: pass
        draw(list_A)
        canvas.update()
        print(f"DEBUG INFO - Shaker Sort")
        print(f"Time Taken {tm.perf_counter() - time1: 0.2f}s")
        set_elements(list_A)
    
    def merge_sort(event):
        global c1, c2
        c1, c2 = 0, 0
        time1 = tm.perf_counter()
        
        set_elements(recursive_merge(elements[::], 0))

        #print(elements)
        #set_elements(elements)
        draw(elements)
        canvas.update()
        print(f"DEBUG INFO - Merge Sort")
        print(f"Time Taken {tm.perf_counter() - time1: 0.2f}s")

    def recursive_merge(array, middle):
        global c1, c2
        #draw((array + elements[len(array)::])[:50:])
        draw(elements)
        canvas.update()
        if len(array) >= 2:
            c2 += 1
            mid = len(array)//2
            left = array[:mid:1]
            right = array[mid::1]
            c1 += 2
            
            recursive_merge(left, mid)
            recursive_merge(right, mid)

            counter1 = counter2 = counter3 = 0

            while counter1 < len(left) and counter2 < len(right):
                c2 += 1
                if left[counter1] < right[counter2]:
                    c2 += 1
                    array[counter3] = left[counter1]
                    c1 += 1
                    counter1 += 1
                else:
                    array[counter3] = right[counter2]
                    c1 += 1
                    counter2 += 1
                counter3 += 1
                #draw((array + elements[len(array)::])[:50:])
                #draw((elements[:middle:]+ array + elements[len(array)::])[:50:])
                canvas.update()

            while counter1 < len(left):
                c2 += 1
                array[counter3] = left[counter1]
                c1 += 1
                counter1 += 1
                counter3 += 1
                #draw((array + elements[len(array)::])[:50:])
                #draw((elements[:middle:]+ array + elements[len(array)::])[:50:])
                canvas.update()

            while counter2 < len(right):
                c2 += 1
                array[counter3] = right[counter2]
                c1 += 1
                counter2 += 1
                counter3 += 1
                #draw((array + elements[len(array)::])[:50:])
                #draw((elements[:middle:]+ array + elements[len(array)::])[:50:])
                canvas.update()
        set_elements((array + elements[len(array)::])[:50:])
        return array
    
    def comb_width(gap):
    
        gap *= 10
        gap //= COMB_SORT_SHRINK_FACTOR
        if gap < 1:
            return 1
        return gap
    
    def comb_sort(event):
        time1 = tm.perf_counter()
        list_A = elements[:]
        writes_to_array = 0
        comparisons = 0
    
        gap = len(list_A)
    
        swapped = True
    
        while gap !=1 or swapped:
            comparisons += 1
            gap = comb_width(gap)
            swapped = False
            for i in range(0, len(list_A)-gap):
                if list_A[i] > list_A[i + gap]:
                    comparisons += 2
                    writes_to_array += 2
                    list_A[i], list_A[i + gap]=list_A[i + gap], list_A[i]
                    swapped = True
                draw(list_A)
                canvas.update()
        draw(list_A)
        canvas.update()
        print(f"DEBUG INFO - Comb Sort")
        print(f"Time Taken {tm.perf_counter() - time1: 0.2f}s")
        set_elements(list_A)

    def counting_sort(list_A, x2):
        n = len(list_A)
        a, b = 0, 0
        return_array = [0] * (n)
        count = [0] * (10)
        for i in range(0, n):
            index = (list_A[i] / x2)
            count[int((index) % 10)] += 1
        for i in range(1, 10):
            b += 1
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            a += 1
            index = (list_A[i] / x2)
            return_array[count[int((index) % 10) ] - 1] = list_A[i]
            count[int((index) % 10)] -= 1
            b += 2
            i -= 1
        i = 0
        for i in range(0, len(list_A)):
            draw(list_A)
            canvas.update()
            list_A[i] = return_array[i]
            a += 1
        return list_A

    def radix_sort(event):
        time1 = tm.perf_counter()
        list_A = elements[:]

        max1 = max(list_A)
        x = 1
        while max1 // x > 0:
            list_A = counting_sort(list_A, x)
            x *= 10
    
        draw(list_A)
        canvas.update()
        set_elements(list_A)
        print(f"DEBUG INFO - Radix Sort")
        print(f"Time Taken {tm.perf_counter() - time1: 0.2f}s")

    draw(elements)
    root.bind("<r>", radix_sort)
    root.bind("<c>", comb_sort)
    root.bind("<b>", bubble_sort)
    root.bind("<m>", merge_sort)
    root.bind("<space>", randomize)
    root.bind("<o>", odd_even_sort)
    root.bind("<s>", shaker_sort)
    root.bind("<C>", rand_col)
    root.mainloop()

if __name__ == "__main__":
    main()
