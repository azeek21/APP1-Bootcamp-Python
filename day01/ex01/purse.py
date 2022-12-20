import typing

# ** operator unpacks the dictionary so we can easily return 
# a copy of a dict by doing return {**mydict}
# to update a key or add a key we can easily do return {**mydict, 'updated_or_new_key': "some_value"}

# we can use single star * operator to unpack lists too. 
# return [*old_list] is equal to returning a new copy of odl_list


def add_ingot(purse: typing.Dict[str, int]):
    return {**purse, 'gold_ingots': purse['gold_ingots'] + 1 if 'gold_ingots' in purse else 1}

def get_ingot(purse: typing.Dict[str, int]):
    return {**purse, 'gold_ingots': purse['gold_ingots'] - 1 if purse['gold_ingots'] >= 1 else 0} if 'gold_ingots' in purse else {**purse}

def empty(purse: typing.Dict[str, int] = 0):
    return {}

if __name__ == "__main__":
    # print(add_ingot(get_ingot(add_ingot(empty({})))))

    purse = empty()
    print(f"Purse now: {purse}")
    for _ in range(10):
        purse = add_ingot(purse)

    print(f"Purse after adding 10 golds: {purse}")

    for _ in range(9):
        purse = get_ingot(purse)
    
    print(f"Purse after getting 9 golds: {purse}")

    for _ in range(200):
        purse = get_ingot(purse)
    
    print(f"Purse after getting 200 golds: {purse}")

    purse = empty()

    print(f"Purse after being emptied: {purse}")

