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

    def convert(self, number: int) -> str:
        return (
            "M" * int(number / 1000)
            + self._convert(numeration=100, number=number % 1000)
            + self._convert(numeration=10, number=number % 100)
            + self._convert(numeration=1, number=number % 10)
        )

    def _convert(self, numeration: int, number: int):
        numeration_symbol = RomanNumeralsConverter._LOOKUP[numeration]
        half_symbol = RomanNumeralsConverter._LOOKUP[numeration * 5]
        if number >= numeration * 5:
            next_numeration = numeration * 10
            return self._to_upper_half(
                number=number,
                numeration=numeration,
                next_numeration=next_numeration,
                numeration_symbol=numeration_symbol,
                next_numeration_symbol=RomanNumeralsConverter._LOOKUP[next_numeration],
                half_symbol=half_symbol,
            )
        return self._to_lower_half(
            number=number,
            numeration=numeration,
            numeration_symbol=numeration_symbol,
            half_symbol=half_symbol,
        )

    def _to_lower_half(
        self,
        number: int,
        numeration: int,
        numeration_symbol: str,
        half_symbol: str,
    ):
        if number % (5 * numeration) >= (4 * numeration):
            return numeration_symbol + half_symbol
        return numeration_symbol * int(number / numeration)

    def _to_upper_half(
        self,
        number: int,
        numeration: int,
        next_numeration: int,
        numeration_symbol: str,
        next_numeration_symbol: str,
        half_symbol: str,
    ) -> str:
        if number >= next_numeration - numeration:
            return numeration_symbol + next_numeration_symbol
        remainder = number - next_numeration / 2
        return half_symbol + numeration_symbol * int(remainder / numeration)
