"""Given a string s, find the length of the longest 
substring without repeating characters."""


    
def LongestSubstring(str):
    l,r = 0,1
    mx = ''
    while(l<r and r<len(str)):
        if str[r] in str[l:r]:
            if r-l > len(mx):
                mx = str[l:r]
                l=r
            print(l,r)
        r += 1
        print(l,r)
    return mx

if __name__ == "__main__":
    s = LongestSubstring('abcdcffd')
    if s == '':
        print("No substring found")
    else:
        print(f"Longest substring without repeating characters is <'{s}'>")
    