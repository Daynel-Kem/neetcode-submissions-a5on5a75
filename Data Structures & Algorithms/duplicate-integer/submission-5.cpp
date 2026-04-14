class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> exists;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = exists.find(nums[i]);
            if (it != exists.end()) { return true; }
            else {
                exists.emplace(nums[i], 1);
            }
        }
        return false;
    }
};