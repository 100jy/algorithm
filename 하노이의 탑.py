n = int(input())
mini = float('inf')

def hanoi(k,arr1,arr2,arr3 ,hist):
    if len(arr3) == n and sorted(arr3,reverse=True) == arr3:
        if k < mini:
            print(0)
            return k, hist
        return

    if arr1[-2] < arr1[-1] or arr2[-2] < arr2[-1] or arr3[-2] < arr3[-1]:
        return

    #1 ->3, 1->2
    tmp = arr1.pop()
    arr3.append(tmp)
    hanoi(k+1, arr1, arr2, arr3, hist.append(1,3))
    hist.pop()
    arr3.pop()
    arr2.append(tmp)
    hanoi(k+1, arr1, arr2, arr3, hist.append(1,2))
    hist.pop()
    arr2.pop()
    arr1.append(tmp)
    # 2 ->1, 2->3
    tmp = arr2.pop()
    arr1.append(tmp)
    hanoi(k+1, arr1, arr2, arr3,hist.append(2,1))
    hist.pop()
    arr1.pop()
    arr3.append(tmp)
    hanoi(k+1, arr1, arr2, arr3, hist.append(2,3))
    hist.pop()
    arr3.pop()
    arr2.append(tmp)
    # 3 ->1, 3->2
    tmp = arr3.pop()
    arr1.append(tmp)
    hanoi(k+1, arr1, arr2, arr3, hist.append(3,1))
    hist.pop()
    arr1.pop()
    arr2.append(tmp)
    hanoi(k+1, arr1, arr2, arr3, hist.append(3,2))
    hist.pop()
    arr2.pop()
    arr3.append(tmp)



answer = hanoi(n,[x for x in range(1,n+1)],[],[],[])

print(answer[0])