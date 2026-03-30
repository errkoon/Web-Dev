def sum13(nums):
    total = 0
    skip_next = False
    for n in nums:
        if skip_next:
            skip_next = False
            continue
        if n == 13:
            skip_next = True
            continue
        total += n
    return total