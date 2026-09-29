class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        # Count vowels in the first window
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for i in range(k, len(s)):

            # Add new character
            if s[i] in vowels:
                count += 1

            # Remove old character
            if s[i - k] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count