import re
with open("sarlija", "r") as f:
    text = f.read()

print(text)

pattern = r'\\\\([^ ]+)'

proc_txt = re.sub(pattern, '', text)

print()
print(proc_txt)
