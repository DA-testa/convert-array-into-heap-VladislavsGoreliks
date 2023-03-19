# python3


def build_heap(data):
    n = len(data)
    swaps = []

    def heapify(i):
        nonlocal swaps
        min_idx = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and data[l] < data[min_idx]:
            min_idx = l
        if r < n and data[r] < data[min_idx]:
            min_idx = r

        if i != min_idx:
            data[i], data[min_idx] = data[min_idx], data[i]
            swaps.append((i, min_idx))
            heapify(min_idx)

    # start from the last parent node
    for i in range(n // 2 - 1, -1, -1):
        heapify(i)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
