from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len: int = 0
        
        # [1] longest substring is the one with the largest 
        #    difference between positions of repeated characters; 
        #    thus, we should create a storage for such positions 
        pos = defaultdict(int)
        
        # [2] while iterating through the string (i.e., moving 
        #    the end of the sliding window), we should also 
        #    update the start of the window 
        start: int = 0
        
        for end, ch in enumerate(s):
            # [3] get the position for the start of sliding window 
            #    with no other occurences of 'ch' in it 
            start = max(start, pos[ch])
            
            # [4] update maximum length 
            max_len = max(max_len, end-start+1)
            
            # [5] set the position to be used in [3] on next iterations
            pos[ch] = end + 1
                
        return max_len
