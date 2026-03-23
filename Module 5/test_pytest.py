def test_num():
    num = int(input("Enter a number greater than zero: "))
    assert num > 0

def test_string():
    string = str(input("Type a sentence! "))
    assert len(string) > 0