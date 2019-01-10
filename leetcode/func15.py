class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ma = {}
        nums.sort()
        for i in range(len(nums)):
            ma[nums[i]] = i

        lis = []
        remi=None
        remj=None
        for i in range(len(nums)):
            if nums[i]==remi:
                continue
            remi=nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == remj:
                    continue
                remj = nums[j]
                a = 0 - nums[i] - nums[j]
                inde = ma.get(a)
                if inde and inde > j:
                    lis.append([nums[i], nums[j], nums[inde]])
        return lis

if __name__ == '__main__':
    inpu=[0,0,0,0]
    retu=Solution().threeSum(inpu)
    print(retu)