class Solution:
    def search(self, nums: List[int], target: int) -> int:
        med= len(nums)//2
        if nums[med] > target:
            for i in range(0,med):
                if nums[i]==target:
                    return i
                
        elif nums[med]==target:
            return med
        
        else:
            for i in range(med,len(nums)):
                if nums[i]==target:
                    return i

        return -1


            
        