import random

starting_phrase = "Reiz kādā tālā zemē..."
continuations = [
    "tur dzīvoja maģisks pūķis.",
    "visi sapņoja par varoņiem.",
    "un visur bija dīvaini radījumi."
]

story = starting_phrase + " " + random.choice(continuations)
print(story)
