class Solution {
public:
    vector<string> ans;
    string path;
    
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        
        vector<string> mp = {
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };
        
        backtrack(0, digits, mp);
        return ans;
    }
    
    void backtrack(int index, string &digits, vector<string> &mp) {
        // Base case
        if (index == digits.length()) {
            ans.push_back(path);
            return;
        }
        
        // Get letters corresponding to current digit
        string letters = mp[digits[index] - '0'];
        
        // Try every possible letter
        for (char ch : letters) {
            path.push_back(ch);
            
            // Move to next digit
            backtrack(index + 1, digits, mp);
            
            // Undo the choice
            path.pop_back();
        }
    }
};