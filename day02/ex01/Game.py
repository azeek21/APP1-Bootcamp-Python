from collections import Counter
from Player import Player

class Game(object):
    
    def __init__(self, matches: int = 10) -> None:
        self.matches = matches
        self.registry = Counter()

    def play(self, p1: Player, p2: Player) -> None:
        p1n = 0
        p2n = 0
        for _ in range(self.matches):
            p1_puts = p1.put_candy()
            p2_puts = p2.put_candy()
    
            if p1_puts and p2_puts:
                self.registry[p1.name] += 2
                self.registry[p2.name] += 2
                p1.get_candy(2)
                p2.get_candy(2)
            elif p1_puts and (not p2_puts):
                self.registry[p1.name] -= 1
                self.registry[p2.name] += 3
                p1.get_candy(0)
                p2.get_candy(3)
            elif (not p1_puts) and p2_puts:
                self.registry[p1.name] += 3
                self.registry[p2.name] -= 1
                p1.get_candy(3)
                p2.get_candy(0)
            elif (not p1_puts) and (not p2_puts):
                p1.get_candy(0)
                p2.get_candy(0)

        p1.reset()
        p2.reset()


    def top3(self):
        for name, score in self.registry.most_common(5):
            print(f"{name} {score}")
