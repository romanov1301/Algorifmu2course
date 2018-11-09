class SortManager:
    compare_num = 0
    swap_num = 0

    @staticmethod
    def compare_count(n):
        SortManager.compare_num += n
        pass

    @staticmethod
    def swap_count(n):
        SortManager.swap_num += n
        pass

    @staticmethod
    def count_reset():
        SortManager.compare_num = 0
        SortManager.swap_num = 0


    @staticmethod
    def insertion_sort(arr):

        for index in range(len(arr) - 1, -1, -1):
            current_value = arr[index].width
            current_index = arr[index]
            position = index
            while position < (
                    len(arr) -
                    1) and arr[position + 1].width > current_value:
                arr[position] = arr[position + 1]
                position += 1
                SortManager.compare_count(2)
            SortManager.compare_count(2)
            SortManager.swap_count(1)
            arr[position] = current_index

        return arr

    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high].length

        for j in range(low, high):

            SortManager.compare_count(1)
            if arr[j].length <= pivot:

                i = i + 1
                SortManager.swap_count(2)
                arr[i], arr[j] = arr[j], arr[i]

        SortManager.swap_count(2)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1





    def quick_sort(arr, low, high):

        if low < high:


            pi = SortManager.partition(arr, low, high)

            SortManager.quick_sort(arr, low, pi - 1)
            SortManager.quick_sort(arr, pi + 1, high)

        return arr