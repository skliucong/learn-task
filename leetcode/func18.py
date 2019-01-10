class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        le=len(nums)
        ma={}
        lis=[]
        nums.sort()
        for i in range(le):
            ma[nums[i]]=i

        remi=None
        remj=None
        remk=None
        for i in range(le-2):
            if remi==nums[i]:
                continue
            remi=nums[i]
            for j in range(i+1,le-1):
                if remj == nums[j]:
                    continue
                remj = nums[j]
                for k in range(j+1,le):
                    if remk == nums[k]:
                        continue
                    remk = nums[k]
                    lev=target-nums[i]-nums[j]-nums[k]
                    if ma.get(lev) and ma.get(lev)>k:
                        lis.append([nums[i],nums[j],nums[k],lev])
                remk=None
            remj=None

        return lis

if __name__ == '__main__':
    nums=[0,1,5,0,1,5,5,-4]
    target=11
    re=Solution().fourSum(nums,target)
    print(re)