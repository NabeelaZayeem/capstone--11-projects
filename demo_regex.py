import re
pattern=r"\bhcl\b"
str="hello hcl hello"
m=re.findall(pattern,str)
print(m)
pattern=r"\d+"
str2="hello 123 22333 "
m2=re.findall(pattern,str2)
print(m2)
pattern=r"\b([a-z]+[a-zA-Z0-9-_.]+@[a-zA-Z]+\.[a-zA-Z]+)\b"
str1="hello nabeela12@gmail.com from hcl nabe121eAlaAAAA12@gmail.cOM hcl 12nabA@gmail.com bangalore hcl"
m1=re.findall(pattern,str1)
print(m1)
pattern=r"(hcl)"
str1="hello from hcl hcl bangalore hcl"
m1=re.findall(pattern,str1)
pattern=r"\d{2}-\d{2}-\d{4} |\d{2}-\w{3}-\d{3}"
str4="02-11-2001 02-nov-2001 02-feb-2023 02/11/2001"
m6=re.findall(pattern,str4)
print(m6)