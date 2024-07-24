from um import count

def main ():

    test_um()

    test_up_low_case()

    test_word_um_plus()

def test_um():

    assert count("um") == 1
    assert count("um, thanks, um...") == 2

def test_up_low_case():

    assert count("UM, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1

def test_word_um_plus():

    assert count("UM, thanks, ummmai") == 1
    assert count("UMas, thanks, ummmai") == 0


if __name__ == "__main__":
    main()
