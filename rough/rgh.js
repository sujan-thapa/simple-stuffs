function lengthOfLongestSubstring(s) {
    let n = s.length;
    let set = new Set();
    let maxLength = 0, i = 0, j = 0;

    while (i < n && j < n) {
        // Try to extend the range [i, j]
        if (!set.has(s[j])) {
            set.add(s[j]);
            j++;
            maxLength = Math.max(maxLength, j - i);
        } else {
            set.delete(s[i]);
            i++;
        }
    }

    return maxLength;
}

// Example 1
let s1 = "abcabcbb";
console.log(lengthOfLongestSubstring(s1)); // Output: 3

// Example 2
let s2 = "bbbbb";
console.log(lengthOfLongestSubstring(s2)); // Output: 1

// Example 3
let s3 = "pwwkew";
console.log(lengthOfLongestSubstring(s3)); // Output: 3
