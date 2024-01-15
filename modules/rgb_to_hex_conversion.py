def extract_hex_code(decimal_number: int) -> str:
    result = hex(decimal_number).replace("0x", "").upper()
    if len(result) == 1:
        return f"0{result}"
    return result


def rgb(red: int, green: int, blue: int) -> str:
    if not isinstance(red, int):
        raise ValueError("❗️ Value for red should be an integer")
    if red > 255:
        raise ValueError("❗️ Value for red should be 255 or less")
    if red < 0:
        raise ValueError("❗️ Value for red should be 0 or greater")
    if not isinstance(green, int):
        raise ValueError("❗️ Value for green should be an integer")
    if green > 255:
        raise ValueError("❗️ Value for green should be 255 or less")
    if not isinstance(blue, int):
        raise ValueError("❗️ Value for blue should be an integer")
    if blue > 255:
        raise ValueError("❗️ Value for blue should be 255 or less")
    return "".join([extract_hex_code(red), extract_hex_code(green), extract_hex_code(blue)])
