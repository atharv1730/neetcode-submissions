class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in checked:
                return [checked.index(difference), i]

            checked.append(nums[i])