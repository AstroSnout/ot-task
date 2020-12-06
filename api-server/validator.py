class Validator:
    @staticmethod
    def is_date(date_string: str) -> bool:
        try:
            # Check if valid string format -> Raises ValueError
            year, month, day = date_string.split('-')
            # Check if digits -> Raises AssertionError
            for x in [year, month, day]:
                assert x.isnumeric(), 'Not a number.'
            # Check if adequate length (YYYY-MM-DD) -> Raises ValueError
            if len(year) != 4 or len(month) != 2 or len(day) != 2:
                raise ValueError('Not enough numbers.')
        except ValueError:
            return False
        except AssertionError:
            return False
        return True

    @staticmethod
    def is_hex_address(hex_address_string: str) -> bool:
        try:
            # Check if hexadecimal -> Raises ValueError
            int(hex_address_string, 16)
        except ValueError:
            return False
        return True
