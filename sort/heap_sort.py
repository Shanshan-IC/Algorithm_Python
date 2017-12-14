def heapify(l, n, i):
    maxs = i
    left = 2*i+1
    right = 2*i+2
    if (left<n and l[left]>l[maxs]):
        maxs = left
    if (right<n and l[right]>l[maxs]):
        maxs = right
    if (maxs!=i):
        l[i], l[maxs] = l[maxs], l[i]
        heapify(l, n, maxs)

def heap_sort(l):
    size = len(l)
    for i in range(size/2-1, -1, -1):
        heapify(l, size, i)
    for j in range(size-1, -1, -1):
        l[0], l[j] = l[j], l[0]
        heapify(l, j, 0)
    return l

def main():
    l = [2, 3, 4, 1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = heap_sort(l)
    print li

main()