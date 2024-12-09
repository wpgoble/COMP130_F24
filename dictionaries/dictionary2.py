def mystery2(table, v):
    for k in table:
        if table[k] == v:
            return k
    print("No such element")
    return None


def mystery(table, v):
    k = input(f"What is associated with {v}? ")
    if k in table and type(table[k]) is not list:
        temp = table[k]
        table[k] = [temp, v]
    elif k in table:
        table[k].append(v)
    else:
        table[k] = v


def mystery3(table):
    print("This table contains")
    print("="*20)
    for k in table:
        if len(k) < 8:
            print(f"{k}\t\t==>\t{table[k]}")
        else:
            print(f"{k}\t==>\t{table[k]}")


if __name__ == "__main__":
    sports = {"baseball":"Phillies", "football":"Eagles", "basketball":"76ers"}
    k =  mystery2(sports, "Union")
    if k is None:
        mystery(sports, "Union")
    mystery3(sports)