def get_words_total_count(contents: str) -> int:
    return len(contents.split())

def get_chars_count(contents: str) -> dict[str, int]:
    chars: dict[str, int] = {}

    for letter in contents:
        lowered = letter.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def get_sorted_char_count(chars_count: dict[str, int]) -> list[dict[str, str | int]]:
    chars_list: list[dict[str, str | int]] = []
    for k, v in chars_count.items():
        chars_list.append({ "char" : k, "num" : v})

    chars_list.sort(key=lambda char: char["num"], reverse=True)
 
    return chars_list
