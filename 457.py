from ast import literal_eval

def longestCommonPrefix(l: list) -> str:
    ans = ""
    l = sorted(l)
    first = l[0]
    last = l[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans

l = literal_eval(input("Enter list of strings: "))
print(longestCommonPrefix(l))