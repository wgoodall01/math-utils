__author__ = 'William'


def part(arr, l, r):
    pivotInd = l+((r-l)//2)

    print('PivotInd: '+ str(pivotInd))
    print('Pivot: arr[ '+ str(pivotInd), '] = '+str(arr[pivotInd]))
    print('Array: '+ str(arr));

    #pivot swap
    piv = arr[pivotInd]
    arr[pivotInd] = arr[l]
    arr[l] = piv

    print('Pivotswapped array: '+ str(arr))

    l = l + 1;

    while(True):
        if r-l <= 1 and arr[l] < arr[r]:
            print("Final arr: " + str(arr))
            print("Divide: " + str(l))
            return l;


        if arr[l] < piv: l += 1
        if arr[r] > piv: r -= 1
        if arr[r] < piv and arr[l] > piv:
            rVal = arr[r]
            arr[r] = arr[l]
            arr[l] = rVal


def partition(A, lo, hi):
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while True:
        do
            j = j - 1
        while A[j] > pivot
        do
            i = i + 1
        while A[i] < pivot
        if i < j
            swap A[i] with A[j]
        else
            return j