import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

# --------- LESK FUNCTION ---------
def lesk_wsd(sentence, target_word):
    context = set(word_tokenize(sentence.lower()))
    senses = wn.synsets(target_word)

    if not senses:
        return "No senses found in WordNet"

    best_sense = None
    max_overlap = 0

    for sense in senses:
        # definition + examples
        gloss = sense.definition() + " " + " ".join(sense.examples())
        gloss_words = set(word_tokenize(gloss.lower()))

        overlap = len(context.intersection(gloss_words))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense


# --------- MAIN PROGRAM ---------

sentence = input("Enter a sentence: ")
target_word = input("Enter target word: ").lower()

sense = lesk_wsd(sentence, target_word)

if isinstance(sense, str):
    print(sense)
else:
    print("\nBest Sense:", sense.name())
    print("Definition:", sense.definition())
    print("Examples:", sense.examples())
