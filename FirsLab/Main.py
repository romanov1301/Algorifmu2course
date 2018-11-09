from SortManager import SortManager
from datetime import datetime


class Sofa(object):
    def __init__(self, width=0, length=0, colour="Red", brand="Dyvan Inc"):
        self.width = width
        self.length = length
        self.colour = colour
        self.brand = brand

    def __str__(self):
        return ("Width: " + str(self.width) + ", Length: " +
                str(self.length) + ", Colour: " + self.colour +
                ", Brand: " + self.brand)


class Main:
    sofa_list = []

    @staticmethod
    def init():
        with open("sofa.txt") as file:
            i = 0
            for line in file:
                array = line.split(",")
                Main.sofa_list.append(Sofa(int(array[0]), int(array[1]), array[2], array[3]))
                i += 1

    @staticmethod
    def print_array(list):
        print("Initial list")
        for arr_i in range(len(list)):
            print(list[arr_i])
        print("\n====================\n")


Main.init()
Main.print_array(Main.sofa_list)

quicksort_arr = Main.sofa_list
insertion_sort_arr = Main.sofa_list


start = datetime.now().microsecond
quicksort_arr = SortManager.quick_sort(Main.sofa_list, 0, len(Main.sofa_list) - 1)
finish = datetime.now().microsecond
print("Quicksort by length:")
print("Time spent: %s mills" % (finish - start))
print("Number of comparisons: " + str(SortManager.compare_num))
print("Number of item swaps: " + str(SortManager.swap_num))

for j in range(len(quicksort_arr)):
    print(quicksort_arr[j])
print("\n====================\n")

SortManager.count_reset()
start = 0
finish = 0


start = datetime.now().microsecond
insertion_sort_arr = SortManager.insertion_sort(Main.sofa_list)
finish = datetime.now().microsecond
print("Insertion sort by width:")
print("Time spent: %s mills" % (finish - start))
print("Number of comparisons: " + str(SortManager.compare_num))
print("Number of item swaps: " + str(SortManager.swap_num))
for j in range(len(insertion_sort_arr)):
    print(insertion_sort_arr[j])
print("\n====================\n")