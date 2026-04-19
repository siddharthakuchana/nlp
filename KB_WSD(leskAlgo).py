sense_dict = {
    "bank": [
        ("finance", "money deposit loan cash account"),
        ("river", "water river shore land edge")
    ],
    "bat": [
        ("animal", "night fly animal wings cave"),
        ("sports", "cricket baseball bat hit ball")
    ],
    "plant": [
        ("factory", "industry factory machines production manufacturing"),
        ("living", "tree green leaves grow soil nature plant")
    ],

    "crane": [
        ("bird", "bird fly wings long neck water"),
        ("machine", "construction lift heavy machine crane building")
    ],

    "match": [
        ("game", "sports game cricket football competition players"),
        ("fire", "stick fire light burn matchbox flame")
    ],

    "mouse": [
        ("animal", "small animal rat tail cheese"),
        ("computer", "device click computer screen pointer mouse")
    ]
}

def simple_lesk(sentence, target_word):
    context = set(sentence.lower().split())

    if target_word not in sense_dict:
        return "No senses available"

    best_sense = None
    max_overlap = 0

    for sense_name, gloss in sense_dict[target_word]:
        gloss_words = set(gloss.split())

        overlap = len(context.intersection(gloss_words))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense_name

    return best_sense


sentence = input("Enter sentence: ")
target_word = input("Enter target word: ").lower()

result = simple_lesk(sentence, target_word)

print("\nBest Sense:", result)
