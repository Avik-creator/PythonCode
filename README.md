# Natural Language Processing Concepts

This repository contains implementations of various Natural Language Processing (NLP) concepts as part of coursework at MAKAUT. These implementations are designed to demonstrate fundamental NLP techniques in Python.

## Current Implementations

### 1. N-gram Language Model ([ngram.py](ngram.py))
An implementation of n-gram language models for text generation.

- Features:
  - Tokenization of text into words
  - Building n-gram models of arbitrary length
  - Text generation from the model using seed phrases
  - Random seed selection option

### 2. TF-IDF Implementation ([tfidf.py](tfidf.py))
A Term Frequency-Inverse Document Frequency (TF-IDF) implementation for document analysis.

- Features:
  - Text tokenization
  - Term Frequency (TF) calculation
  - Inverse Document Frequency (IDF) calculation
  - TF-IDF scoring for terms across multiple documents

## Setup

This project uses a Python virtual environment in the `.nlp` directory. To activate the environment:

```bash
# On macOS/Linux
source .nlp/bin/activate

# On Windows
.\.nlp\bin\activate.bat
```

## Planned Implementations

Future additions to this repository may include:
- Text classification algorithms
- Named Entity Recognition (NER)
- Sentiment analysis
- Word embeddings
- Topic modeling
- Machine translation concepts
- Text summarization techniques

## Usage Examples

### N-gram Model

```python
from ngram import tokenize, build_ngram_model, generate_text

# Sample text
text = "Natural language processing is a subfield of linguistics, computer science, and artificial intelligence."

# Tokenize the text
tokens = tokenize(text)

# Build a bi-gram model
n = 2
model = build_ngram_model(tokens, n)

# Generate text using the model
seed = ("natural", "language")
generated_text = generate_text(model, n, seed, length=10)
print(generated_text)
```

### TF-IDF

```python
from tfidf import tokenize, calculate_tf, calculate_idf, calculate_tfidf

# Sample documents
documents = [
    "This is a sample document about NLP.",
    "NLP is used for text analysis.",
    "Document classification is an application of NLP."
]

# Tokenize documents
tokenized_docs = [tokenize(doc) for doc in documents]

# Calculate IDF
idf = calculate_idf(tokenized_docs)

# Calculate TF-IDF for the first document
tf = calculate_tf(tokenized_docs[0])
tfidf = calculate_tfidf(tf, idf)
print(tfidf)
```