
def subarray_sum(nums):
    sum = 0
    hs = {0: -1}
    for i in xrange(len(nums)):
        sum += nums[i]
        if sum in hs:
            return [hs[sum]+1, i]
        hs[sum] = i
    return
