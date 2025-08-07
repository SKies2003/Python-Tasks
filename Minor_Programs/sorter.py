def sorter(lst: list) -> list:
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i+1] < lst[i]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

if __name__ == "__main__":
    nums = [1, 2, 4, 2, 8, 9, 2, 3, 4, 7, 6, 1, 9, 9, 2]
    print(sorter(nums))