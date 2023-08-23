def strcounter(s):
    for lit in s:
        counter = 0
        for sub_lit in s:
            if lit == sub_lit:
                counter +=1
        print(lit, counter)
strcounter("aabcd")


def strcounter(s):
    for lit in set(s):
        counter = 0
        for sub_lit in s:
                if lit == sub_lit:
                    counter +=1
        print(lit, counter)



strcounter()


