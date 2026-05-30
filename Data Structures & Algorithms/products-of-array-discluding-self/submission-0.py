class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        result = []
        count = 0
        for i in nums:
            if i == 0:
                count += 1
            else:
                prod *= i
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if count > 0:
                    result.append(0)
                else:
                    result.append(prod // nums[i])
            else:
                if count == 1:
                    result.append(prod)
                else:
                    result.append(0)


        return result