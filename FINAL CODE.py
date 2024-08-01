# Import libraries
import numpy as np
import cv2
import time
import random

def partition(arr, low, high):
    pivot = arr[high][1]
    i = low - 1
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def radix(dict):
    m = max(dict.values())
    exp = 1
    while exp <= m:
        di = [[] for _ in range(10)]
        for key, value in dict.items():
            digit = (value // exp) % 10
            di[digit].append((key, value))
        dict = {k: v for b in di for k, v in b}
        exp *= 10
    return dict

def bucket(d):
    
    items = list(d.items())

    # Applying bucket sort based on the values
    max1 = max(item[1] for item in items)
    buckets = [[] for _ in range(max1 + 1)]
    for k, v in items:
        buckets[v].append((k, v))

    sitems = []
    for bucket in buckets:
        sitems.extend(bucket)

    # Converting the sorted list back into a dictionary
    sdict = dict(sitems)
    return sdict



# Function to generate random dictionary with given size
def generate_random_dict(size):
    return {i: random.randint(1, 1000) for i in range(size)}


# Empty dictionary  
d={}

#Array contains path of 30 images
p=np.array(['IMG2.jpg','IMG1.jpg','IMG11.jpg','IMG13.jpg','img3.jpg','IMG4.jpg','IMG5.jpg','IMG6.jpg','IMG7.jpg','IMG8.jpg','IMG9.jpg','IMG10.jpg','IMG12.jpg','IMG14.jpg','IMG15.jpg','IMG16.jpg','IMG17.jpg','IMG18.jpg','IMG19.jpg','IMG20.jpg','IMG21.jpg','IMG22.jpg','IMG23.jpg','IMG24.jpg','IMG25.jpg','IMG26.jpg','IMG27.jpg','IMG28.jpg','IMG29.jpg','IMG30.jpg'])
n=[]

# Loading images
for i in p:
    img = cv2.imread(i)
    img = cv2.resize(img,(640,800))


    # Preparing images - blur and convert them to grey scale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grey, (17, 17), 0)


    # Showing blurred images and grey scaled images
   # cv2.imshow("Grey scale", grey)
   # cv2.imshow("Blurred", blurred)
   # cv2.waitKey(0)


    # Canny edge detector
    outline = cv2.Canny(blurred, 30, 150)


    # Showing canny edge detector
   # cv2.imshow("Edges", outline)
   # cv2.waitKey(0)


    # Finding the contours
    (cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


    # Drawing contours: -1 will draw all contours
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
   # cv2.imshow("Result", img)
   # cv2.waitKey(0)
    n.append(len(cnts))

# Inserting all the data in dictionary
for k,v in zip(p,n):
    d[k]=v

# Sorting the items in dictionary using quick sort
it = list(d.items())
quicksort(it, 0, len(it) - 1)
print("Sorted images using quick sort: ")
for j in it:
    print(j[0], ":", j[1])
print('\n')

# Sorting the items in dictionary using radix sort
s= radix(d)
print("Sorted images using radix sort: ")
for k1,v1 in s.items():
    print(k1,":",v1)
print('\n')


# Sorting the items in dictionary using bucket sort
sdict = bucket(d)
print("Sorted images using bucket sort: ")
for k2,v2 in sdict.items():
    print(k2,":",v2)
print('\n')


# Measuring the  execution time for different input sizes
for input_size in range(100, 1100, 100):
    # Generate random dictionary
    dictionary = generate_random_dict(input_size)

    # time for radix
    st = time.time()
    sorted_dict = radix(dictionary.copy())
    et = time.time()
    rtime = et - st


    #  time for partition and quicksort
    arr = list(dictionary.items())
    st1 = time.time()
    quicksort(arr, 0, len(arr) - 1)
    et1 = time.time()
    qtime = et1 - st1

    # time for bucket sort
    st2 = time.time()
    sorted_dict = bucket(dictionary.copy())
    et2 = time.time()
    btime = et2 - st2

    print(f"Input size: {input_size}, Radix sort time: {rtime} seconds, Quicksort time: {qtime} seconds, Bucket sort: {btime}")