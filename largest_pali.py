#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
find largest palindrome
"""
def longestPalindrome(str):
    longest = ""
   
    for idx, c in enumerate(str):
        """ case for even number strings
        """
        tempStr = ""
        tempStr = findLongest(str, idx, idx)
        if len(tempStr) > len(longest):
            longest = tempStr
        
        """ case for odd number string
        """
        tempStr = findLongest(str, idx, idx+1)
        if len(tempStr) > len(longest):
            longest = tempStr
    return longest

def findLongest(str, left, right):
    """ finds the longest palindrome from the center to the left and right
    """
    while left >= 0 and right < len(str):
        if str[left] != str[right]:
            break
        left -= 1
        right += 1
    return(str[left+1:right])

if __name__ == '__main__':
    print(longestPalindrome('abba'))
    print(longestPalindrome('adbaab'))
    print(longestPalindrome('abic'))
    print(longestPalindrome('abababababababababa'))
    print(longestPalindrome('bababababababababa'))