"""Challenge 4 - String manipulation."""


def main() -> None:
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    print("Number of words:", len(words))
    print("Reversed sentence:", " ".join(reversed(words)))
    print("Modified sentence:", sentence.replace(" ", "-"))


if __name__ == "__main__":
    main()
