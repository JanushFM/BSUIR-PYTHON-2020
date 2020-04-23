import os
import sys
import random
import tempfile

const_one_GB = 1073741824
list_of_runs = []  # Variable to get access for temp files


def external_sort(unsorted_file_name, sorted_file_name):
    divide_f_to_parts(unsorted_file_name)
    merging()
    copy_temp_to_main(sorted_file_name)


def divide_f_to_parts(file_path):
    temp_array = []

    if not os.path.exists(file_path):
        raise FileNotFoundError("File {0} not found.".format(file_path))
    size = os.path.getsize(file_path)
    with open(file_path, "r") as f:
        for line in f:
            temp_array.append(int(line))
            if len(temp_array) >= 10000:
                division(temp_array)
        if len(temp_array) != 0:
            division(temp_array)


def division(temp_array):
    merge_sort(temp_array)
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp:
        temp.writelines("{}\n".format(i) for i in temp_array)
        list_of_runs.append(temp)
    temp_array.clear()


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) >> 1  # mid = len(arr)//2
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge_sorted_files(temp, file1, file2):
    line_from_file1 = file1.readline()
    line_from_file2 = file2.readline()

    while line_from_file1 and line_from_file2:  # bool('')== False
        if int(line_from_file1) > int(line_from_file2):
            temp.writelines(line_from_file2)
            line_from_file2 = file2.readline()
        else:
            temp.writelines(line_from_file1)
            line_from_file1 = file1.readline()

    while line_from_file1:
        temp.writelines(line_from_file1)
        line_from_file1 = file1.readline()

    while line_from_file2:
        temp.writelines(line_from_file2)
        line_from_file2 = file2.readline()


def delete_file_from_list(file):
    if os.path.exists(file.name):
        list_of_runs.pop(0)
        os.remove(file.name)
    else:
        raise FileNotFoundError("File {0} not found.".format(file))


def merging():
    while len(list_of_runs) > 1:
        with open(list_of_runs[0].name, "r") as file_1, open(list_of_runs[1].name, "r") as file_2:
            with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp:
                merge_sorted_files(temp, file_1, file_2)
                list_of_runs.append(temp)
        delete_file_from_list(file_1)
        delete_file_from_list(file_2)


def copy_temp_to_main(name_of_sorted_file):  # sorted and merged file
    temp = list_of_runs[0]
    with open(name_of_sorted_file, "w") as sorted_file:
        with open(temp.name, "r") as temp_file:
            sorted_file.writelines("{}".format(i) for i in temp_file)
    delete_file_from_list(temp)


