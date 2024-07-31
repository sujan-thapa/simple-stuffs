# Given a string s, find the length of the longest substring without repeating characters.


def indexSlicing(s):
    # return 
    maxLength = 0
    i = 0
    j = 0
    lis = set()
    # print(len(s))
    while (i<len(s) and j < len(s)):
        if(s[j] not in lis):
            lis.add(s[j])
            j +=1
            maxLength = max(maxLength, j-i)
            # print(maxLength)
        else:
            lis.remove(s[i])
            i +=1
    
    # return maxLength
    print(maxLength)

s = "abcabcbb"

indexSlicing(s)
s2 = "bbbbb";
# print(b)
indexSlicing(s2)

s3 = "pwwkew"
indexSlicing(s3)

# f (!set.has(s[j])) {
#             set.add(s[j]);
#             j++;
#             maxLength = Math.max(maxLength, j - i);
#         } else {
#             set.delete(s[i]);
#             i++;