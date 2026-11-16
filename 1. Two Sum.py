nums=[2,7,11,15]
target=9
for i in range(0, len(nums)-1):
    if (nums[i] + nums[i+1]==target):
        print([i,i+1])
    