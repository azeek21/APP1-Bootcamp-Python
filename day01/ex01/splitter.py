import typing
import math

def split_booty(*purses: typing.Dict[str, int]) -> typing.Tuple[typing.Dict[str, int], ...]:
    gold_total = sum([i.get('gold_ingots') for i in purses if 'gold_ingots' in i])
    print(gold_total, end='\n\n\n')

    res = []

    for _ in range(3):
        res.append({'gold_ingots': math.ceil(gold_total / 3) if gold_total % 3 != 0 else int(gold_total / 3)})
        if gold_total % 3 != 0:
            gold_total -= 1

    return tuple(res)


if __name__ == "__main__":
    split_purses = split_booty({'gold_ingots': 1}, {'gold_ingots': 2}, {'gold_ingots': 102})
    print(split_purses)

