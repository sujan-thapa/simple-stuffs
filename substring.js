// Given a string s, find the length of the longest substring without repeating characters.

// let s = "abcabcbb";

function getAllSubstrings(str) {
    let substrings = [];

    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j <= str.length; j++) {
            substrings.push(str.slice(i, j));
        }
    }

    return substrings;
}

let str = "sujan";
console.log(getAllSubstrings(str));

