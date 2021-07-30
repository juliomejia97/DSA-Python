def findPythagoreanTriplets(nums):
    c = set()
    for i in nums:
        c.add(i**2)
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            if((a**2)+(b**2)) in c:
                return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
