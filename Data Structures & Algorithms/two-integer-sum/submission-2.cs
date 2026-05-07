public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] solution = new int[2];
        Dictionary<int, int> correspondingNums = new Dictionary<int, int>();
        
        for (int i = 0; i < nums.Length; ++i)
        {
            if (correspondingNums.ContainsKey(nums[i]))
            {
                solution[0] = correspondingNums[nums[i]];
                solution[1] = i;

                return solution;
            }
            
            correspondingNums.Add(target - nums[i], i);
        }

        return solution;
    }
}
