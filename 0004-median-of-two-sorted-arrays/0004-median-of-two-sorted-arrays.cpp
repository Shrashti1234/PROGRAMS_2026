class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        // Always binary search on the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();

        int low = 0;
        int high = m;

        while (low <= high) {

            int i = (low + high) / 2;

            int j = (m + n + 1) / 2 - i;

            // Left side values
            int left1;
            int left2;

            if (i == 0)
                left1 = INT_MIN;
            else
                left1 = nums1[i - 1];

            if (j == 0)
                left2 = INT_MIN;
            else
                left2 = nums2[j - 1];


            // Right side values
            int right1;
            int right2;

            if (i == m)
                right1 = INT_MAX;
            else
                right1 = nums1[i];

            if (j == n)
                right2 = INT_MAX;
            else
                right2 = nums2[j];


            // Correct partition
            if (left1 <= right2 && left2 <= right1) {

                // Total number of elements is odd
                if ((m + n) % 2 == 1) {
                    return max(left1, left2);
                }

                // Total number of elements is even
                else {
                    return (
                        max(left1, left2) +
                        min(right1, right2)
                    ) / 2.0;
                }
            }

            // Too many elements taken from nums1
            else if (left1 > right2) {
                high = i - 1;
            }

            // Too few elements taken from nums1
            else {
                low = i + 1;
            }
        }

        return 0.0;
    }
};