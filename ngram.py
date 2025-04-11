import random
from collections import defaultdict

def tokenize(text):
    """
    Tokenizes the input text into words and removes punctuation.
    """
    return text.lower().split()

def build_ngram_model(tokens, n):
    model = defaultdict(list)
    for i in range(len(tokens)-n):
        key = tuple(tokens[i:i+n])
        next_token = tokens[i+n]
        model[key].append(next_token)
    return model

def generate_text(model, n, seed=None, length=20):
    if seed is None:
        seed = random.choice(list(model.keys()))
        print("Random seed chosen:", seed)
    elif isinstance(seed, str):
        seed = tuple(seed.lower().split())
        if len(seed) != n:
            raise ValueError(f"Seed must be of length {n}, got {len(seed)}")
    
    output = list(seed)
    for _ in range(length):
        key = tuple(output[-n:])
        print("Generated Text key", key)
        possible_next = model.get(key)
        if not possible_next:
            break
        next_token = random.choice(possible_next)
        output.append(next_token)
    return ' '.join(output)

if __name__ == '__main__':
    text = """
    The sun rises in the east. The sun sets in the west.
    The moon shines at night. The stars twinkle beautifully.
    Nature is peaceful and calming. The sun, the moon, and the stars dance together in the sky.
    """

    n = int(input("Enter the value of n for n-grams: "))
    tokens = tokenize(text)
    print(f"Tokens: {tokens}")
    ngram_model = build_ngram_model(tokens, n)
    print(f"N-gram model: {ngram_model}")
    seed = input("Enter a seed phrase (or leave blank for random): ")
    if seed:
        seed = seed.split()
    else:
        seed = None

    print(f"Seed: {seed}")
    length = int(input("Enter the length of the generated text: "))
    generated_text = generate_text(ngram_model, n, seed, length)
    print(f"Generated text: {generated_text}")