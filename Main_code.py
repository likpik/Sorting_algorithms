import time
import random
import copy
import sys
sys.setrecursionlimit(10000)

print("Podaj algorytm sortowania: \n merge sort - ms \n heap sort - hs \n bubble sort - bs")
print(" selection sort - ss \n insertion sort - is \n quick sort - qs")
s = input()
print("Podaj rodzaj listy: \n 0 - liczby losowe (10 elementowa) \n 1 - liczby losowe \n 2 - liczby rosnące")
print(" 3 - liczby malejące \n 4 - A-kształtna \n 5 - V-kształtna")
rodzaj = input()
if rodzaj != '0':
    print("Podaj ilość elementów tablicy: ")
    n = int(input())
else:
    n = 10

losowa10 = [4, 1, 5, 2, 9, 8, 7, 3, 10, 6]

losowa = []
for i in range(n):
    losowa.append(random.randint(1, n))

rosnaca = []
for i in range(n):
    rosnaca.append(i)

malejaca = []
for i in range(n):
    malejaca.append(n-i)

A_ksztaltna = []
for i in range(n//2):
    A_ksztaltna.append(i)
for i in range(n//2):
    A_ksztaltna.append(n//2-i)

V_ksztaltna = []
for i in range(n//2):
    V_ksztaltna.append(n//2-i)
for i in range(n//2):
    V_ksztaltna.append(i)

if rodzaj == '0':
    A = losowa10
elif rodzaj == '1':
    A = losowa
elif rodzaj == '2':
    A = rosnaca
elif rodzaj == '3':
    A = malejaca
elif rodzaj == '4':
    A = A_ksztaltna
elif rodzaj == '5':
    A = V_ksztaltna

if n == 10:
    print('poczatkowa tablica: ', A)

liczba_p = 0; liczba_z = 0

def msort(array):
    global liczba_p
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        msort(L)
        msort(M)
        i = j = k = 0

        while i < len(L) and j < len(M):
            liczba_p += 1
            if L[i] > M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

    return array

def heapify(array, n, i):
    global liczba_p
    global liczba_z
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[l] < array[smallest]:
        smallest = l
        liczba_p += 1

    if r < n and array[r] < array[smallest]:
        smallest = r
        liczba_p += 1

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        liczba_z += 1
        heapify(array, n, smallest)

def heapSort(array):
    n = len(array)

    for i in range(n//2, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array

def partition(array, low, high):
    global liczba_p
    global liczba_z
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        liczba_p += 1
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            liczba_z += 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    if len(array) == 10:
        print("pivot: ", pivot)
    return i + 1


def qsort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        qsort(array, low, pi - 1)
        qsort(array, pi + 1, high)
    return array

if s == 'bs':
    st1 = time.time()
    A1 = copy.deepcopy(A)
    for j in range(1, len(A1)-1):
        for i in range(len(A1)-j):
            liczba_p += 1
            if A1[i] < A1[i+1]:
                A1[i], A1[i+1] = A1[i+1], A1[i]
                liczba_z += 1
    end1 = time.time()
    time1 = end1 - st1
    print('czas: ', time1)

elif s == 'is':
    st1 = time.time()
    A1 = copy.deepcopy(A)
    for j in range(1, len(A1)):
        key = A1[j]
        i = j - 1
        liczba_z += 1
        while i >= 0 and A1[i] < key:
            A1[i + 1] = A1[i]
            i -= 1
            liczba_p += 1
        A1[i + 1] = key
    end1 = time.time()
    time1 = end1 - st1
    print('czas: ', time1)

elif s == 'ss':
    st1 = time.time()
    A1 = copy.deepcopy(A)
    for j in range(len(A1) - 1):
        min = j
        for i in range(j + 1, len(A1)):
            #liczba_p += 1
            if A1[i] > A1[min]:
                min = i
                liczba_p += 1
        A1[min], A1[j] = A1[j], A1[min]
        liczba_z += 1
    end1 = time.time()
    time1 = end1 - st1
    print('czas: ', time1)

elif s == 'qs':
    st1 = time.time()
    A1 = copy.deepcopy(A)
    qsort(A1, 0, len(A1)-1)
    end1 = time.time()
    time1 = end1 - st1
    print('czas: ', time1)

elif s == 'ms':
    st1 = time.time()
    A1 = copy.deepcopy(A)
    msort(A1)
    end1 = time.time()
    time1 = end1 - st1
    print('czas: ', time1)


elif s == 'hs':
    st1 = time.time()
    A1 = copy.deepcopy(A)
    heapSort(A1)
    end1 = time.time()
    time1 = end1 - st1
    print('czas: ', time1)


if n == 10:
    print('posortowana tablica: ', A1)
print('liczba porownan: ', liczba_p)
if s != 'ms':
    print('liczba zamian elementow: ', liczba_z)
k = liczba_p + liczba_z
print('laczna liczba zamian i porownan elementow: ', k)
