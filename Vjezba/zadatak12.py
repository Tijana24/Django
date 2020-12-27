# izvlacenje potpuno parnih petocifrenih brojeva(brojevi cija je svaka cifra parna)

new_list =[] # A list which holds the numbers
for a in range(11111,99999):
    for b in str(a):
        if int(b) % 2 != 0:
            break
    else:
        # only executed if the loop wasn't broken out of
        new_list.append(a)

print(new_list)