class RomanNumeralsConverter:

    _LOOKUP = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    def __init__(self, number: int):
        self._number = number

    def convert(self) -> str:
        return (
            "M" * int(self._number / 1000)
            + self._convert(numeration=100)
            + self._convert(numeration=10)
            + self._convert(numeration=1)
        )

    def _convert(self, numeration: int):
        self._number %= numeration * 10
        numeration_symbol = RomanNumeralsConverter._LOOKUP[numeration]
        half_numeration = numeration * 5
        half_symbol = RomanNumeralsConverter._LOOKUP[half_numeration]
        if self._number >= half_numeration:
            return self._to_upper_half(
                numeration=numeration,
                numeration_symbol=numeration_symbol,
                half_symbol=half_symbol,
            )
        return self._to_lower_half(
            numeration=numeration,
            numeration_symbol=numeration_symbol,
            half_symbol=half_symbol,
        )

    def _to_upper_half(
        self,
        numeration: int,
        numeration_symbol: str,
        half_symbol: str,
    ) -> str:
        next_numeration = numeration * 10
        next_numeration_symbol = RomanNumeralsConverter._LOOKUP[next_numeration]
        if self._number >= next_numeration - numeration:
            return numeration_symbol + next_numeration_symbol
        remainder = self._number - next_numeration / 2
        return half_symbol + numeration_symbol * int(remainder / numeration)

    def _to_lower_half(
        self,
        numeration: int,
        numeration_symbol: str,
        half_symbol: str,
    ):
        if self._number % (5 * numeration) >= (4 * numeration):
            return numeration_symbol + half_symbol
        return numeration_symbol * int(self._number / numeration)
