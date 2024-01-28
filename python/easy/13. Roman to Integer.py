class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev = 0

        for i in s:
            val = translations[i]

            if val > prev:
                total += val - 2 * prev
            else:
                total += val
            prev = val

        return total

# create an instance of the class
a = Solution()

# call the method
print(a.romanToInt("MCMXCIV"))
