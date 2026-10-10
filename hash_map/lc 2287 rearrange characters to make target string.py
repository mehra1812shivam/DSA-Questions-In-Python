class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_map={}
        target_map={}
        for ch in s:
            s_map[ch]=s_map.get(ch,0)+1
        for ch in target:
            target_map[ch]=target_map.get(ch,0)+1
        min_value=float('inf')
        for ch in target_map.keys():
            if ch in s_map:
                min_value=min(min_value,s_map[ch]//target_map[ch])
            else:
                return 0
        return min_value