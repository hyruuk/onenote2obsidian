import os 
import os.path as op
import string


def list_notes(input_folder):
    """Returns a list of notes in the input folder"""
    notes = []
    for root, dir, files in os.walk(input_folder):
        for file in files:
            if file != []:
                notes.append(op.join(root,file))
    return notes

def get_words(notes):
    """Returns a list of words in the notes"""
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    allwords = []
    for note in notes:
        with open(note, "r") as f:
            words = f.read().split()
            for word in words:
                # Check if all characters of word are in alphabet
                if all(char in alphabet for char in word):
                    # Keep only words longer than 2 characters
                    if len(word) > 2:
                        allwords.append(word)
                        print(word)

    # Clean up words list
    return allwords

def process_words(allwords):
    """Detects key words in the list of words"""
    words, counts = np.unique(allwords, return_counts=True)
    sorted_counts = sorted(counts)
    words_sorted_by_count = [words[x] for x in np.argsort(counts)]

    
    return key_words

if __name__== "__main__":

    input_folder = "input"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Get list of notes
    notes = list_notes(input_folder)
    allwords = get_words(notes)


    words, counts = np.unique(allwords, return_counts=True)
    sorted_counts = sorted(counts)
    words_sorted_by_count = [words[x] for x in np.argsort(counts)]




