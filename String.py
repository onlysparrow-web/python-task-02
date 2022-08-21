# Capitalize
text = "pradeep"
x = text.capitalize()
print(x)
# CaseFold
text = "PRADEEP"
x = text.casefold()
print(x)
# Center
text = "PRADEEP"
x = text.center(20, "-")
print(x)
# Count
text = "PRADEEP study's python and practice python"
x = text.count("python")
print(x)
# Encode
text = "PRADEEP study's python and practice python"
x = text.encode()
print(x)
# Endwith
text = "PRADEEP study's python and practice python"
x = text.endswith("n")
print(x)
# Expandtabs
text = "H\te\tl\tl\to"
x = text.expandtabs(2)
print(x)
# Find
text = "PRADEEP study's python and practice python"
x = text.find("python")
print(x)
# index
text = "PRADEEP study's python and practice python"
x = text.find("P")
print(x)
# isalnum
text = "PRADEEP13"
x = text.isalnum()
print(x)
# asalpha
text = "PRADEEP12"
x = text.isalpha()
print(x)
# ascii
text = "PRADEEP12"
x = text.isascii()
print(x)
# isdecimal
text = "1.2"  # "\u0033"
x = text.isdecimal()
print(x)
# isdigit
text = "12"  # "\u0033"
x = text.isdigit()
print(x)
# identifier
text = "call12"  # "\u0033"
x = text.isidentifier()
print(x)
# lower
text = "pradep"
x = text.islower()
print(x)
# trip
text = "..okyespradep"
x = text.lstrip("..okyes")
print(x)
# maketrans
text = "pradep Nes"
x = text.maketrans("N", "Y")
print(text.translate(x))
# partition
text = "pradep is learning python"
x = text.partition("learning")
print(x)
# replace
text = "pradep is learning is python"
x = text.replace("learning", "practicing")
print(x)
# rfind
text = "pradep is learning is python"
x = text.rfind("is")
print(x)
# rindex
text = "pradep is learning is python"
x = text.rindex("is")
print(x)
# rjust
text = "pradep"
x = text.rjust(20)
print(x)
# rpartition
text = "pradep is learning is python"
x = text.rpartition("is")
print(x)
# rsplit
text = "pradep"
x = text.rsplit(", ")
print(x)
# startswith
text = "pradep is learning is\npython"
x = text.startswith("pradep")
print(x)
# swapcase
text = "Pradep is Learning is Python"
x = text.swapcase()
print(x)
# title
text = "pradep is learning ispython"
x = text.title()
print(x)
# upper
text = "pradep is learning is python"
x = text.upper()
print(x)
# zfill
text = "7"
x = text.zfill(3)
print(x)
