import re 

s="hii bie chai letter lofie toffee tiffin food chick"
x=re.findall(r'[a-z]{3,4}',s)

print(x)