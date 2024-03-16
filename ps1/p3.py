s = "azcbobobegghakl"

a = s[0]
i = 0
s_len = len(s)
while i < s_len:
    ii = i
    while ii < s_len:
        ii += 1
        if sorted(s[i : ii + 1]) != list(s[i : ii + 1]) or ii == s_len:
            if len(a) < ii - i:
                a = s[i:ii]
            break
    i = ii

print("Longest substring in alphabetical order is: " + str(a))
