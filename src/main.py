# -*- coding: utf-8 -*-
"""Main script for Multilingual PDF RAG System"""

import os
from src.text_extraction import extract_text
from src.preprocessing import clean_text, detect_language, chunk_text
from src.embedding_index import add_documents_to_index
from src.retrieval import initialize_bm25, answer_query_with_memory


def main():
    # Example usage

    # List of PDF paths (Update with your PDF paths)
    pdf_paths = ['https://github.com/Anishvjy/Multilingual-pdf-rag-system/blob/main/data/sample_pdfs_rag/sample_pdfs/bn/Blue_Ocean_Strategy%2C_Expanded_Edition_How_to_Create_Uncontested-2.pdf']

    # Initialize an empty string to hold all extracted text
    all_extracted_text = ""

    # Extract text from all PDFs
    for pdf_path in pdf_paths:
        if pdf_path.endswith('.pdf') and os.path.exists(pdf_path):
            try:
                extracted_text = extract_text(pdf_path)
                all_extracted_text += extracted_text
            except Exception as e:
                print(f"Error extracting text from {pdf_path}: {e}")
        else:
            print(f"Invalid or missing PDF path: {pdf_path}")

    # Clean the extracted text
    cleaned_text = clean_text(all_extracted_text)
    print("Extracted and cleaned text length:", len(cleaned_text))

    # Detect language
    language = detect_language(cleaned_text)
    print(f"Detected language: {language}")

    # Chunk the cleaned text
    chunks = chunk_text(cleaned_text)
    print("Number of chunks:", len(chunks))

    # Add chunks to FAISS index
    add_documents_to_index(chunks)

    # Initialize BM25 for keyword-based search
    bm25 = initialize_bm25(chunks)

    # User query
    query = input("Enter your query: ")
    response = answer_query_with_memory(query, chunks, bm25)
    print("Answer:", response)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
