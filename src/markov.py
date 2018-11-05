import random, re, sys

def markov_mappings(text, prefix_word_count):
    words = re.split("\\s+", text)
    count = len(words)
    for i in range(prefix_word_count, count):
        suffix = words[i + 1] if i < (count - 1) else None
        yield tuple(words[i - prefix_word_count:i + 1]), suffix

def markov_table(text, prefix_word_count):
    table = {}
    for prefix, suffix in markov_mappings(text, prefix_word_count):
        suffixes = table.get(prefix, [])
        if suffix:
            suffixes.append(suffix)
        table[prefix] = suffixes
    return table

def markov_generate(text, max_words):
    table = markov_table(text, prefix_word_count=10)
    prefix = random.choice(list(table.keys()))
    suffix = None
    result = prefix[0] + " " if prefix else ""
    i = 0
    while prefix and i < max_words:
        suffix = random.choice(table[prefix])
        next_prefixes = list(pair for pair in table.keys() if suffix in pair)
        prefix = random.choice(next_prefixes) if next_prefixes else None
        if prefix:
            result += " ".join(prefix) + " "
        i += 1
    return result

if len(sys.argv) < 2:
    print("Syntax: python markov.py <filepath>")
else:
    print(markov_generate(open(sys.argv[1], mode="r", encoding="utf-8").read(), max_words=200))
