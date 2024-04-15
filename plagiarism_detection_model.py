#importing libraries for model building

import os

import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

os.chdir("/content/Test")

#code to seprate text and images from word docx

from docx import Document
from docx.shared import Inches
import io
import os

def extract_images_and_text(doc_path):
    doc = Document(doc_path)
    image_dir = os.path.join(os.path.dirname(doc_path), "images")
    os.makedirs(image_dir, exist_ok=True)

    for rel in doc.part.rels.values():
        if "image" not in rel.reltype:
            continue
        image_data = rel._target._blob
        image_ext = os.path.splitext(rel._reltype)[1]
        image_path = os.path.join(image_dir, f"{rel.rId}{image_ext}")

        with open(image_path, "wb") as img_file:
            img_file.write(image_data)

    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

    with open('text.txt', 'w') as f:
        f.write(text)
    return "text.txt"

# Call the function with your docx file
for file in os.listdir():
  if file.endswith(".docx"):
    text = extract_images_and_text(file)
    named_text = str(file[:-5])
    named_text = named_text + ".txt"
    os.rename(text,named_text)

# moving text file to a different location

import os
import shutil

def move_txt_files(source_dir, target_dir):
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):
            # Construct full file path
            source = os.path.join(source_dir, filename)
            target = os.path.join(target_dir, filename)
            # Move the file
            shutil.move(source, target)

# Call the function with your directories
move_txt_files('/content/Test', '/content/Test/Text files')

os.chdir("/content/Test/Text files")

# Get a list of student files
student_file = [file for file in os.listdir() if file.endswith('.txt')]

# Read the content of each student's file

student_docs = [open(file).read() for file in student_file]

# Print the list of student files and their content

for filename, document in zip(student_file, student_docs):

    print(f"File: {filename}")

    print("Content:")

    print(document)

    print("-" * 30)  # Separator between documents

# Function to create TF-IDF vectors from a list of documents

def create_tfidf_vectors(docs):

    return TfidfVectorizer().fit_transform(docs).toarray()

# Function to calculate cosine similarity between two document vectors

def calc_cosine_similarity(vector1, vector2):

    return cosine_similarity([vector1, vector2])

# Create TF-IDF vectors for the student documents

doc_vec = create_tfidf_vectors(student_docs)
# Pair each document with its corresponding filename

doc_filename_pairs = list(zip(student_file, doc_vec))

# Function to check for plagiarism

def find_plagiarism():

    # Initialize an empty set to store plagiarism results

    plagiarism_results = set()


    # Access the global variable doc_filename_pairs

    global doc_filename_pairs


    # Iterate through each student's file and vector

    for student_a_file, student_a_vec in doc_filename_pairs:

        # Create a copy of the document-filename pairs for iteration

        remaining_pairs = doc_filename_pairs.copy()


        # Find the index of the current document-filename pair

        current_index = remaining_pairs.index((student_a_file, student_a_vec))


        # Remove the current pair from the remaining pairs

        del remaining_pairs[current_index]


        # Iterate through the remaining pairs to compare with other students

        for student_b_file, student_b_vec in remaining_pairs:

            # Calculate the cosine similarity between student_a_vec and student_b_vec

            similarity_score = calc_cosine_similarity(student_a_vec, student_b_vec)[0][1]


            # Sort the filenames to maintain consistency in results

            sorted_filenames = sorted((student_a_file, student_b_file))


            # Create a plagiarism result tuple with sorted filenames and similarity score

            plagiarism_result = (sorted_filenames[0], sorted_filenames[1], similarity_score)


            # Add the result to the plagiarism_results set

            plagiarism_results.add(plagiarism_result)


    # Return the set of plagiarism results

    return plagiarism_results


# Print plagiarism results

plagiarism_results = find_plagiarism()


for result in plagiarism_results:
  print(result)

file = input()
file = file.replace("docx","txt")
coun = 0
for reports in plagiarism_results:
  if file in reports:
    if float(reports[2]) > 0.098:
      print(reports[0],reports[1], reports[2]*100, "%")
      coun += 1
if coun < 1:
  print("Non Plag")