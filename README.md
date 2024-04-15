# Text-Plagiarism-Test
Used for calculating the similarity between a list of text files using TF-IDF vectors &amp; Cosine Similarity

Cosine similarity is a mathematical metric used to measure the similarity between two vectors in a multi-dimensional space, particularly in high-dimensional spaces. It calculates the cosine of the angle between the vectors. Let’s dive into the details:


Cosine Similarity Formula:
Given two vectors A and B, the cosine similarity between them is calculated as:
similarity(A,B)=cos(θ)=∥A∥∥B∥A⋅B​
Here:

(A \cdot B) represents the dot product of vectors A and B.
(|A|) and (|B|) denote the magnitudes (lengths) of vectors A and B, respectively.



Application in Text Analysis:

In text analysis, documents are often converted into vectors. Each dimension of the vector corresponds to a word from the document, with its value indicating the frequency or importance of that word.
Cosine similarity allows us to compare documents based on their word representations, regardless of the specific details of each data point.
It is widely used in natural language processing (NLP), search algorithms, and recommendation systems.



Example:
Imagine you and your friend have rated three books on a scale of 1 to 5:

Your ratings: [5, 3, 4]
Your friend’s ratings: [4, 2, 4]

To quantitatively measure how similar your ratings are, you can use cosine similarity. Calculate the cosine similarity between your vectors:
similarity([5,3,4],[4,2,4])=52+32+42​⋅42+22+42​5⋅4+3⋅2+4⋅4​
The resulting value will indicate the similarity between your preferences for those books1.


Cosine similarity is a powerful tool for understanding relationships between data points, especially in the context of text analysis and high-dimensional spaces. It helps us find semantic similarities without being tied to specific data representations
