class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        char_to_word_mapping = {}
        word_to_char_mapping = {}

        for char, word in zip(pattern, words):
            if char not in char_to_word_mapping:
                char_to_word_mapping[char] = word
            elif word != char_to_word_mapping[char]:
                return False

            if word not in word_to_char_mapping:
                word_to_char_mapping[word] = char
            elif char != word_to_char_mapping[word]:
                return False

        return True


a = Solution()

print(a.wordPattern("abba", "dog cat cat dog"))