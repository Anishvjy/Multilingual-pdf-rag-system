# -*- coding: utf-8 -*-
"""chunking.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ypn1RzqVXVVd4JJjFbDt0yflg8IJYOLU
"""

def chunk_text(text, max_length=500):
    # Split text into sentences using regex
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    chunks = []
    current_chunk = ""
    # Combine sentences into chunks of specified max length
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks