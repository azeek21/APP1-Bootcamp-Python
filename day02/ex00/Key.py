
class Key(object):

    def __init__(self) -> None:
        self.passphrase = "zax2rulez"
        self.len = 1337
    

    def __str__(self):
        return "GeneralTsoKeycard"

    def __len__(self):
        return 1337

    def __getitem__(self, index):
        if index == 404:
            return 3
        else:
            raise IndexError

    def __gt__(self, x):
        if x == 9000:
            return True
        return False

