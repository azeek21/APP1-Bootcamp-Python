from Key import Key

def __test_success(key: Key):
    print("TEST: __test_success >>>\n")
    print("Start assertion test")

    assert len(key) == 1337, "len(key) == 1337"
    assert key[404] == 3, "key[404] == 3"
    assert key > 9000, "key > 9000"
    assert key.passphrase == "zax2rulez", "key.passphrase == \"zax2rulez\""
    assert str(key) == "GeneralTsoKeycard", "str(key) == \"GeneralTsoKeycard\""

    print("Finish assertion, SUCCESS !")


def __test_fail(key: Key):
    print("TEST: __test__fail >>>\n")
    print("Start assertion test")

    assert len(key) == 1237, "len(key) == 1337"
    assert key[404] == 4, "key[404] == 3"
    assert key > 9001, "key > 9000"
    assert key.passphrase == "ax2rulez", "key.passphrase == \"zax2rulez\""
    assert str(key) == "eneralTsoKeycard", "str(key) == \"GeneralTsoKeycard\""

    print("Finish assertion, Fail !")



if __name__ == "__main__":
    key = Key()

    __test_success(key)
