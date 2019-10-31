if __name__ == '__main2__':
    n = int(input())
    # map(function, other_iterable_list)
    # map return a object
    arr = list(map(int, input().split()))
    # print(arr)
    # to convert it into list we do: list(map(function,list))
    print(list(arr))
    arr = [57,-57,57,57]
    arr.sort()
    for i in range(-1, -len(arr)-1, -1):
        print(i)
        if arr[i] != max(arr):
            print(arr[i])
            break
    print(arr[i] for i in range(-1, -len(arr), -1) if arr[i] != max(arr))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(-1, -len(arr)-1, -1):
        if arr[i] != max(arr):
            print(arr[i])
            break

