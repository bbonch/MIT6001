s = "azcbobobegghakl"
vowels = ["a", "e", "i", "o", "u"]
count = 0
for l in s:
    if l in vowels:
        count += 1

print("Number of vowels: " + str(count))
