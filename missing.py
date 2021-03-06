"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

    # solution 1
    
    # set_nums = set(nums)

    # for num in range(1, max_num + 1):
    #     if num not in set_nums:
    #         return num


    # solution 2
    # 
    # nums.sort()
    # 
    # for num in nums:
    #     if nums[nums.index(num) + 1] and num == nums[nums.index(num) + 1] - 1:
    #         continue
    #     else:
    #         return num + 1


    # solution 3
    
    should_be = (max_num * (1 + max_num))/2
    actually = sum(nums)
    return int(should_be - actually)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
