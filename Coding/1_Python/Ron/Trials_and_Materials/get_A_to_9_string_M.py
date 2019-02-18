
def letters():
    # make all letter as a string
    upper_case_letter = "".join(chr(character) for character in range(65,90+1))
    lower_case_letter = "".join(chr(character) for character in range(97,122+1))
    numeric_letter = "".join(chr(character) for character in range(48,57+1))
    all_letter_string=upper_case_letter+lower_case_letter+numeric_letter

    print(upper_case_letter)
    print(lower_case_letter)
    print(numeric_letter)
    print(all_letter_string)

if __name__ == "__main__":
    letters()
