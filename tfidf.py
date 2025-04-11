import math
from collections import Counter

def tokenize(text):
    """
    Tokenizes the input text into words and removes punctuation.
    """
    # Convert to lowercase and split by whitespace
    tokens = text.lower().split()
    # Remove punctuation
    tokens = [word.strip('.,!?;:"()[]{}') for word in tokens]
    return tokens


def calculate_tf(document_tokens):
    """
    Calculates the term frequency (TF) for each word in the document.
    """

    tf = {}
    total_terms = len(document_tokens)
    term_counts = Counter(document_tokens)
    for(term, count) in term_counts.items():
        tf[term] = count / total_terms
    return tf

def calculate_idf(documents):
    """
    Calculates the inverse document frequency (IDF) for each word in the corpus.
    """
    N = len(documents)
    idf = {}
    all_tokens = set()
    
    # Count the number of documents containing each term
    term_doc_count = Counter()
    for document in documents:
        unique_terms = set(document)
        all_tokens.update(unique_terms)
        for term in unique_terms:
            term_doc_count[term] += 1

    # Calculate IDF for each term
    for term in all_tokens:
        idf[term] = math.log(N / (1 + term_doc_count[term]))

    return idf

def calculate_tfidf(documents, idf):
    tfidf = {}
    for term, tf_value in documents.items():
        tfidf[term] = tf_value * idf[term]
    return tfidf

def main():
    documents = [
        "The quick brown fox jumps over the lazy dog.",
        "The dog barks at the fox.",
        "The fox is quick and clever.",
        "A lazy dog lies in the sun."
    ]

    tokenized_documents = [tokenize(doc) for doc in documents]

    print("Tokenized Documents:")
    for doc in tokenized_documents:
        print(doc)
    
    idf = calculate_idf(tokenized_documents)
    print("\nInverse Document Frequency (IDF):")
    for term, value in idf.items():
        print(f"{term}: {value:.4f}")
    print("\nTerm Frequency (TF):")
    for i, doc in enumerate(tokenized_documents):
        tf = calculate_tf(doc)
        print(f"Document {i+1}:")
        for term, value in tf.items():
            print(f"{term}: {value:.4f}")
    print("\nTF-IDF:")

    for i, token in enumerate(tokenized_documents):
        tf = calculate_tf(token)
        tfidf = calculate_tfidf(tf, idf)
        print(f"Document {i+1}:")
        for term, value in tfidf.items():
            print(f"{term}: {value:.4f}")
if __name__ == "__main__":
    main()