class RomanNumeralsConverter:

    def convert(self, number: int) -> str:
        return ("M" * int(number / 1000)
                + self._convert_hundreds(number=number % 1000)
                + self._convert_tens(number=number % 100)
                + self._convert_units(number=number % 10))

    def _convert_units(self, number: int) -> str:
        if number >= 5:
            return self._to_upper_half(
                number=number,
                numeration=1,
                next_numeration=10,
                numeration_symbol="I",
                next_numeration_symbol="X",
                half_symbol="V",
            )
        return self._to_lower_half(
            number=number,
            numeration=1,
            numeration_symbol="I",
            half_symbol="V",
        )

    def _convert_tens(self, number: int) -> str:
        if number >= 50:
            return self._to_upper_half(
                number=number,
                numeration=10,
                next_numeration=100,
                numeration_symbol="X",
                next_numeration_symbol="C",
                half_symbol="L",
            )
        return self._to_lower_half(
            number=number,
            numeration=10,
            numeration_symbol="X",
            half_symbol="L",
        )

    def _convert_hundreds(self, number: int) -> str:
        if number >= 500:
            return self._to_upper_half(
                number=number,
                numeration=100,
                next_numeration=1000,
                numeration_symbol="C",
                next_numeration_symbol="M",
                half_symbol="D",
            )
        return self._to_lower_half(
            number=number,
            numeration=100,
            numeration_symbol="C",
            half_symbol="D",
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
