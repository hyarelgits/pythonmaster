v = ["a","e","i","o","u"]

s = "12345"

for c in s:
    if c in v:
        print("vowel found")
        break
else:
    print("vowel not found")

