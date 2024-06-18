# Textual Document Similitude Test
Uses TF-IDF vectors from a list of documents followed by cosine similarity between two document vectors

## TF-IDF Vectors
- **TF-IDF (_Term Frequency-Inverse Document Frequency_)** is a widely used statistical method in natural language processing and information retrieval.
- **TF** of a term (or word) in a document is the **_number of times_** that term appears in the document, **_normalized_** by the total number of terms in the document.
- **IDF** reflects the proportion of documents in the entire corpus that contain the term. Words unique to a small percentage of documents (e.g., technical jargon terms) receive higher importance values than words common across all documents (e.g., “a,” “the,” and other stop words).
- A high TF-IDF score indicates that a term occurs frequently in a specific document but rarely in other documents.
In other words, it balances the term’s commonality within a document (measured by TF) with its rarity across documents (measured by IDF).
## Cosine Similarity
In text analysis, documents are often converted into vectors. Each dimension of the vector corresponds to a word from the document, with its value indicating the frequency or importance of that word.
Cosine similarity allows us to compare documents based on their word representations, regardless of the specific details of each data point.
### Prerequisite Packages ###
1. scikit-learn
2. python-docx
### Libraries Used ###
1. python-docx
2. scikit-learn
3. io
4. os
5. shutil
