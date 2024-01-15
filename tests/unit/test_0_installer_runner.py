import pytest
from modules import rgb_to_hex_conversion


def describe_rgb():
    def should_error_when_first_input_is_not_integer():
        """🧪 should error if any of the first input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Value for red should be an integer"):
            rgb_to_hex_conversion.rgb("blah", 2, 2)

    def should_error_when_second_input_is_not_integer():
        """🧪 should error if any of the second input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Value for green should be an integer"):
            rgb_to_hex_conversion.rgb(2, "blah", 2)
