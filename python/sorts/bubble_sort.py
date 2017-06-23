
def bubbleSort(toSort):
    swapped = True
    n = len(toSort)
    while swapped:
        swapped = False
        for i in range(1,len(toSort)):
            if toSort[i-1] > toSort[i]:
                toSort[i], toSort[i-1] = toSort[i-1], toSort[i]
                swapped = True
        n = n - 1
    return toSort

if __name__ == "__main__":
    toSort = input("Please enter numbers to sort seperated by a space: ")
    toSort = [int(i) for i in toSort.split()]
    print(bubbleSort(toSort))
