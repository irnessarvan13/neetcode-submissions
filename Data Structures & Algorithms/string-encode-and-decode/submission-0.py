class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            length = len(s)
            result += f'{length}#{s}'
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
    
        while i < len(s):
            j = s.find('#', i)          # find the # starting from i
            length = int(s[i:j])        # extract the length number
            word = s[j+1 : j+1+length]  # grab exactly length characters
            result.append(word)          # add word to result
            i = j + 1 + length          # move i to start of next word
    
        return result
