class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        # ::-1 reverses the string
        if x == x[::-1]:
            return True

        return False


# Create an object of the class
a = Solution()

# Call the isPalindrome function and print the result
print(a.isPalindrome(121))
