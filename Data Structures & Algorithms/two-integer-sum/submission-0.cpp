class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        stable_sort(nums.begin(), nums.end());
        int i = 0;
        int j = nums.size() - 1;
        int sum = 0;
        while (j >= 0 && i < nums.size()) {
            sum = nums[i] + nums[j];
            if (sum == target && i != j) {
                return {i, j};
            } else if (sum > target) {
                j--;
            } else {
                i++;
            }
        }
        return {0,0};
    }
};
