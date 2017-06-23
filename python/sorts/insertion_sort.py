def insertionSort(toSort):
    size = len(toSort)

    for i in range(1,size):
        j = i
        while j > 0 and toSort[j-1] > toSort[j]:
            toSort[j-1], toSort[j] = toSort[j], toSort[j-1]
            j -= 1
    return toSort


if __name__ == "__main__":
    toSort = input("Please enter numbers to sort seperated by a space: ")
    toSort = [int(i) for i in toSort.split()]
    print(insertionSort(toSort))
