def extract_hex_code(decimal_number: int) -> str:
    result = hex(decimal_number).replace("0x", "").upper()
    if len(result) == 1:
        return f"0{result}"
    return result


colours = {0: "red", 1: "green", 2: "blue"}


def rgb(red: int, green: int, blue: int) -> str:
    for index, color in enumerate([red, green, blue]):
        if not isinstance(color, int):
            raise ValueError(f"❗️ Value for {colours[index]} should be an integer")
        if color > 255:
            raise ValueError(f"❗️ Value for {colours[index]} should be 255 or less")
        if color < 0:
            raise ValueError(f"❗️ Value for {colours[index]} should be 0 or greater")
    return "".join([extract_hex_code(red), extract_hex_code(green), extract_hex_code(blue)])
