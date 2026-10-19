class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_dict:dict = {}
        for i, char in enumerate(magazine):
            count_dict[char] = count_dict.get(char, 0) + 1 
        for j, char in enumerate(ransomNote):
            if (char not in count_dict):
                return False
            elif (char in count_dict):
                if (count_dict[char] == 0):
                    return False
                else:
                    count_dict[char] += -1
        return True 
