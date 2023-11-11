set1 = set([i for i in input("Input sequence1: ") if i.isnumeric()])
set2 = set([i for i in input("Input sequence2: ")if i.isnumeric()])

print(len(set1 & set2)>0)