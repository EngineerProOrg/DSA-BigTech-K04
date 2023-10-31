# Array - Live Coding Solutions

Speaker: Hiệp

## [1. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int pmin = prices[0]; // minimum price before day i
        int n = prices.size();
        int result = 0;
        for (int i = 1; i < n; ++i) {
            if (prices[i] - pmin > result) {
                result = prices[i] - pmin;
            }

            if (prices[i] < pmin) {
                pmin = prices[i];
            }
        }
        return result;
    }
};
```

Complexity:

- Time: O(n).
- Space: O(1).

## [2. Remove Element](https://leetcode.com/problems/remove-element/description/)

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0; // number of elements != val
        for (int x: nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

Complexity:

- Time: O(n).
- Space: O(1).

## [3. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result(numRows);
        for (int i = 0; i < numRows; ++i) {
            result[i].resize(i + 1);
            result[i][0] = result[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1];
            }
        }
        return result;
    }
};
```

Complexity:

- Time: O(numRows^2).
- Space: O(numRows^2).

## [4. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int s = 0; // sum of all elements
        for (int x: nums) {
            s += x;
        }

        int n = nums.size();
        int left = 0; // sum of elements before i
        for (int i = 0; i < n; ++i) {
            if (2 * left == s - nums[i]) {
                return i;
            }
            left += nums[i];
        }

        return -1;
    }
};
```

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int right = 0; // sum of elements to the right of i
        for (int x: nums) right += x;

        int left = 0; // sum of elements to the left of i
        for (int i = 0; i < nums.size(); ++i) {
            right -= nums[i];
            if (left == right) return i;
            left += nums[i];
        }
        return -1;
    }
};
```

Complexity:

- Time: O(n).
- Space: O(1).