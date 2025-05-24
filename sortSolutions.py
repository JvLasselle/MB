def insertSort(sortMe):
    for i in range(len(sortMe)):
        if i == 0:
            continue
        if sortMe[i] > sortMe[i-1]:
            continue
        else:
            pointer = i-1
            while pointer >= 0 and sortMe[pointer] > sortMe[pointer+1]:
                temp = sortMe[pointer]
                sortMe[pointer] = sortMe[pointer+1]
                sortMe[pointer+1] = temp
                pointer = pointer-1
    return sortMe

def selectSort(sortMe):
    smallest = None
    smallestLocation = None
    for i in range(len(sortMe)):
        smallest = sortMe[i]
        smallestLocation = i
        for j in range(i+1, len(sortMe)):
            if sortMe[j] < smallest:
                smallestLocation = j
                smallest = sortMe[j]
            sortMe[smallestLocation] = sortMe[i]
            sortMe[i] = smallest
    return sortMe

def mergeSort(sortMe):
    if not len(sortMe) > 1:
        return sortMe
    front = mergeSort(sortMe[0 : len(sortMe)//2])
    back = mergeSort(sortMe[len(sortMe)//2 : len(sortMe)])

    returnMe = []

    while len(front) > 0 and len(back) > 0:
        if front[0] < back[0]:
            returnMe.append(front.pop(0))
        else:
            returnMe.append(back.pop(0))
    returnMe.extend(front)
    returnMe.extend(back)
    return returnMe