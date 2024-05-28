import pytest

from pykatas.roman_numerals import RomanNumeralsConverter


@pytest.mark.parametrize(
    "number, expected_result",
    [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (10, "X"),
        (11, "XI"),
        (12, "XII"),
        (20, "XX"),
        (21, "XXI"),
        (30, "XXX"),
        (31, "XXXI"),
        (50, "L"),
        (51, "LI"),
        (60, "LX"),
        (61, "LXI"),
        (100, "C"),
        (110, "CX"),
        (111, "CXI"),
        (200, "CC"),
        (500, "D"),
        (600, "DC"),
        (620, "DCXX"),
        (621, "DCXXI"),
        (1000, "M"),
        (2000, "MM"),
        (2100, "MMC"),
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (41, "XLI"),
        (90, "XC"),
        (91, "XCI"),
        (400, "CD"),
        (410, "CDX"),
        (900, "CM"),
        (910, "CMX"),
    ]
)
def test_convert_a_number_should_return_a_matching_roman_numeral(
    number,
    expected_result,
):
    converter = RomanNumeralsConverter()
    result = converter.convert(number=number)

    assert result == expected_result
