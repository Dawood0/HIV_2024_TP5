def test_strong_password_checker(strong_password_checker):
    assert strong_password_checker("a") == 5
    assert strong_password_checker("aA1") == 3
    assert strong_password_checker("aA1") == 0
    assert strong_password_checker("1337C0d3") == 0
    assert strong_password_checker("abcdefghijklmnopqrstuvwxyz") == 0
    assert strong_password_checker("abcabcabc") == 2
    assert strong_password_checker("1337") == 3
    assert strong_password_checker("aaaaaaaaaaaa") == 2
    assert strong_password_checker("aA1") == 3
    assert strong_password_checker("a") == 5
    assert strong_password_checker("1337") == 3
    assert strong_password_checker("aA1") == 3
    assert strong_password_checker("aA1") == 0
    assert strong_password_checker("aA1") == 3
    assert strong_password_checker("1337C0d3") == 0
    assert strong_password_checker("abcdefghijklmnopqrstuvwxyz") == 0
    assert strong_password_checker("abcabcabc") == 2
    assert strong_password_checker("1337C0d3") == 0
    assert strong_password_checker("aA1") == 3
    assert strong_password_checker("aaaaaaaaaaaa") == 2
    assert strong_password_checker("aaaaaaaaaaaa") == 2
    assert strong_password_checker("abcabcabcc") == 1
    assert number_to_words(1000) == "One Thousand"
    assert number_to_words(1000) == "One Thousand"
    assert number_to_words(0) == "Zero"
    assert number_to_words(0) == "Zero"
    assert number_to_words(10) == "Ten"
    assert number_to_words(0) == "Zero"
    assert number_to_words(1000) == "One Thousand"
    assert number_to_words(0) == "Zero"
    assert number_to_words(0) == "Zero"
    assert number_to_words(1000) == "One Thousand"
