"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# Additional stories added

new_story = Story(
    ['noun', 'color', 'plural_noun', 'verb', 'adjective'],
    """Once there was a sensitive {noun} that loved its {color} {plural_noun}.
    One day, the {plural_noun} decided to {verb}. The {noun} felt {adjective}."""
)

next_story = Story(
    ['noun', 'color_1', 'color_2', 'color_3', 'verb_1', 'verb_2', 'verb_3', 'place'],
    """The {color_1} {noun} wants to {verb_1}. The {color_2} {noun} wants to {verb_2}. 
    The {color_3} {noun} wants to {verb_3}. Instead, they go to {place}."""
)

camping = Story(
    ['noun_1', 'noun_2', 'noun_3', 'noun_4', 'adjective_1', 'adjective_2', 'verb'],
    """A tall {noun_1} and a short {noun_2} went camping. They brought a big {adjective_1}
    {noun_3} for sleeping and a small {noun_4} to {verb} the campfire. It was {adjective_2}.
    """
)

walk = Story(
    ['adjective_1', 'adjective_2', 'adjective_3',
    'adjective_4', 'noun_1', 'noun_2', 'plural_noun', 'verb'],
    """A jolly {adjective_1} {noun_1} and a grouchy {adjective_2} {noun_2} went for a walk.
    They saw a family of {adjective_3} {plural_noun} about to {verb}. 
    They thought the {plural_noun} were {adjective_4}."""
)

story_map = {
    "Set the Scene": story, 
    "Observation": new_story, 
    "Resolution": next_story,
    "Camping": camping,
    "The Walk": walk
    }