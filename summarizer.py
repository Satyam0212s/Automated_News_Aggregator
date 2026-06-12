from collections import Counter
import re

def summarize(text):

    sentences = text.split(".")

    if len(sentences) <= 2:
        return text

    words = re.findall(r'\w+', text.lower())

    freq = Counter(words)

    sentence_scores = {}

    for sentence in sentences:
        score = 0

        for word in sentence.lower().split():
            score += freq.get(word,0)

        sentence_scores[sentence] = score

    best_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:2]

    return ". ".join(best_sentences)