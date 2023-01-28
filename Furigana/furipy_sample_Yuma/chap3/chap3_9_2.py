teams = ['A', 'B', 'C', 'D', 'E']
for t1 in teams:
    for t2 in teams:
        if t1 != t2:
            print(t1, 'vs', t2)