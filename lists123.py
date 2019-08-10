a=[23,45,23,23,65,45,25]
#b=[j for j in a]
#print(b)
b=[j if a.count(j)>=2 else j*2 for j in a]
print(b)

print("Saved the Lists Successfully!")