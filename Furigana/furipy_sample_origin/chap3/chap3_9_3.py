teams = ['A', 'B', 'C', 'D', 'E']
opps = ['A', 'B', 'C', 'D', 'E']
for t1 in teams:
    opps.remove(t1)
    for t2 in opps:
        print(t1, 'vs', t2)
