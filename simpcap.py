""""
Simple script to capatlize whatever I have on my clipboard
4/17/24
J. Chanenson
""""
import re
import tkinter as tk

def convert_to_title_case(text):
    # Define words to be lowercased unless they are the first word or after a punctuation
    lower_case_words = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'by', 'of', 'in', 'with']

    # Define punctuation characters
    punctuation = '.!?'

    # Split text into words
    words = re.split(r'(\s+|\b)', text)

    # Capitalize appropriate words
    title_case_text = ''
    for i, word in enumerate(words):
        #if word.lower() in lower_case_words and (i == 0 or words[i-1] in punctuation):
        if word.lower() in lower_case_words and (i == 0 or (i > 0 and words[i-1] in punctuation)):

            title_case_text += word.lower()
        else:
            title_case_text += word.capitalize()

    return title_case_text

def main():
    # Initialize tkinter
    root = tk.Tk()
    root.withdraw()

    # Get text from clipboard
    clipboard_text = root.clipboard_get()

    # Convert text to title case
    title_case_text = convert_to_title_case(clipboard_text)

    # Replace clipboard with title case text
    root.clipboard_clear()
    root.clipboard_append(title_case_text)
    root.update()

if __name__ == "__main__":
    main()
