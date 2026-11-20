"""Challenge 2 - Palindrome checker."""


def is_palindrome(text: str) -> bool:
    # Ignore case, spaces and punctuation so phrases like
    # "A man, a plan, a canal: Panama" also work.
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def main() -> None:
    text = input("Enter a string : ")
    if is_palindrome(text):
        print(f"The string '{text}' is a palindrome.")
    else:
        print(f"The string '{text}' is not a palindrome.")


if __name__ == "__main__":
    main()
