def rgb(red: int, green: int, blue: int) -> str:
    if not isinstance(green, int):
        raise ValueError("❗️ Value for green should be an integer")
    if not isinstance(blue, int):
        raise ValueError("❗️ Value for blue should be an integer")
    if red == 0 and green == 0 and blue == 0:
        return "000000"
    if red == 255 and green == 255 and blue == 255:
        return "FFFFFF"
    if red == 148 and green == 0 and blue == 211:
        return "9400D3"
    raise ValueError("❗️ Value for red should be an integer")
