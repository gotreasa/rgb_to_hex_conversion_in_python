import pytest
from modules import rgb_to_hex_conversion


def describe_rgb_guardians():
    def should_error_when_first_input_is_not_integer():
        """🧪 should error if any of the first input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Value for red should be an integer"):
            rgb_to_hex_conversion.rgb("blah", 2, 2)

    def should_error_when_second_input_is_not_integer():
        """🧪 should error if any of the second input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Value for green should be an integer"):
            rgb_to_hex_conversion.rgb(2, "blah", 2)

    def should_error_when_third_input_is_not_integer():
        """🧪 should error if any of the third input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Value for blue should be an integer"):
            rgb_to_hex_conversion.rgb(2, 2, "blah")


def describe_rgb():
    def should_return_000000():
        """🧪 should return 000000 for 0, 0, 0"""
        assert rgb_to_hex_conversion.rgb(0, 0, 0) == "000000"

    def should_return_ffffff():
        """🧪 should return ffffff for 255, 255, 255"""
        assert rgb_to_hex_conversion.rgb(255, 255, 255) == "ffffff"
