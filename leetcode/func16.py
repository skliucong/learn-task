class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_same=999999999
        le=len(nums)
        for i in range(le-2):
            start=i+1
            end=le-1
            su=0
            while start<end:
                su=nums[i]+nums[start]+nums[end]
                if abs(su - target) < abs(min_same):
                    min_same = su - target
                if su==target:
                    return target
                elif su<target:
                    start=start+1
                elif su>target:
                    end=end-1
        return target+min_same





if __name__ == '__main__':
    inpu=[1,2,5,10,11]
    target=12
    res=Solution().threeSumClosest(inpu,target)
    print(res)