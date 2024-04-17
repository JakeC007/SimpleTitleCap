""""
Simple script to capatlize whatever I have on my clipboard
4/17/24
J. Chanenson
"""
import re, time
import tkinter as tk

def punc_check(word):
    """
    Checks for punctuation in a word.

    Args:
    word (str): The word to be checked for punctuation.

    Returns:
    bool: True if the word ends with punctuation, False otherwise.
    """

    # Define the regular expression pattern
    pattern = r'\w+|[^\w\s]'
    
    # Find all matches in the word
    matches = re.findall(pattern, word)
    
    # Check if the last character is punctuation
    if len(matches) > 0:
        last_char = matches[-1]
        if last_char not in [".", "!", "?"]:
            return False
    return True

def convert_to_title_case(text):
    """
    Convert a given text to title case, where the first letter of each word is capitalized,
    except for certain words specified in lower_case_words list, unless they are the first word
    or after a punctuation.

    Args:
    - text (str): The input text to be converted to title case.

    Returns:
    - str: The text converted to title case.
    """
    # Define words to be lowercased unless they are the first word or after a punctuation
    lower_case_words = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'by', 'of', 'in', 'with']
    
    # Split text into words
    words = re.findall(r'\S+|\s', text)

    # Capitalize appropriate words
    title_case_text = ''

    # Check if relevant word is at the start of a sentance
    for i, word in enumerate(words):
        punc = False 
        if word.lower() in lower_case_words and i !=0:
            punc = punc_check(words[i-2])

        if word.lower() in lower_case_words and i != 0 and (i > 0 and not punc):

            title_case_text += word.lower()
        else:
            title_case_text += word.capitalize()

    return title_case_text

def main():

    # Initialize tkinter
    root = tk.Tk()
    root.withdraw()

    # Get text from clipboard
    clipboard_text = root.clipboard_get().strip()

    # Convert text to title case
    title_case_text = convert_to_title_case(clipboard_text)

    # Replace clipboard with title case text
    root.clipboard_clear()
    root.clipboard_append(title_case_text)
    root.update()
    root.mainloop()

if __name__ == "__main__":
    main()
