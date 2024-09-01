#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> sum_indices;
        
        for(int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if(nums.at(i) + nums.at(j) == target) {
                    sum_indices.push_back(i);
                    sum_indices.push_back(j);
                }
            }
        }

        return sum_indices;
    }
};