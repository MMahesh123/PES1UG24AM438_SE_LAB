def format_bib_name(name):
    """
    Upper-cases a runner's name and limits it to 12 characters.
    Invalid inputs return an empty string.
    """
    if not isinstance(name, str):
        return ""
    return name.strip().upper()[:12]


def parse_finish_time(text):
    """
    Converts H:MM:SS into seconds.
    Returns None for invalid input.
    """
    if not isinstance(text, str):
        return None

    parts = text.strip().split(":")
    if len(parts) != 3:
        return None

    try:
        hours, minutes, seconds = (int(part) for part in parts)
    except ValueError:
        return None

    if hours < 0 or not 0 <= minutes < 60 or not 0 <= seconds < 60:
        return None

    return hours * 3600 + minutes * 60 + seconds


def average_split(text):
    """
    Averages non-negative integer split times.
    Returns None for invalid or empty input.
    """
    if not isinstance(text, str):
        return None

    parts = text.split()
    if not parts:
        return None

    try:
        splits = [int(part) for part in parts]
    except ValueError:
        return None

    if any(value < 0 for value in splits):
        return None

    return sum(splits) / len(splits)


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    result = parse_finish_time(value)
    print("Finish time in seconds:", result if result is not None else "Invalid time")

    print("\n==== Running average_split ====")
    value = input(
        "Enter your 5 km split times in minutes separated by spaces "
        "(e.g. 25 26 24): "
    )
    result = average_split(value)
    print(
        "Average split (minutes):",
        result if result is not None else "Invalid split times",
    )


if __name__ == "__main__":
    main()
