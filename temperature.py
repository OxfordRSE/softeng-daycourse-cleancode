def celsius_to_fahrenheit(celsius):
    return 32 + 1.8 * celsius


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(1.0) == 33.8
    assert celsius_to_fahrenheit(12.34) == 54.212
