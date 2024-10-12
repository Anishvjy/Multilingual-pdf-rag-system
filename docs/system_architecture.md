# System Architecture for Multilingual PDF RAG System

## Overview
The system processes multilingual PDFs, extracts text, and uses a Retrieval-Augmented Generation (RAG) approach to answer queries. It integrates various components such as OCR, preprocessing, chunking, indexing, and query handling.

## Architecture Diagram
[ PDF Files ] --> [ Text Extraction (OCR + Digital) ] --> [ Preprocessing ] ↓ [ FAISS Index ] <------> [ Hybrid Search (FAISS + BM25) ] <------> [ Query Handling ] ↓ [ Answer Generation with Memory ]


## Key Components
1. **Text Extraction**: 
   - Extracts text from scanned PDFs using OCR.
   - Extracts text from digital PDFs using PyMuPDF.

2. **Preprocessing**:
   - Cleans and tokenizes the extracted text.
   - Chunks large text into smaller, meaningful segments.

3. **Indexing**:
   - Uses FAISS for semantic search.
   - Uses BM25 for keyword-based search.

4. **Query Handling**:
   - Accepts user queries and retrieves relevant chunks.
   - Combines results from both FAISS and BM25 for better accuracy.

5. **Chat Memory**:
   - Maintains a history of queries to provide context-aware responses.

## Future Improvements
- **Multilingual Embeddings**: Use more optimized multilingual models.
- **Model Optimization**: Implement smaller and faster models to reduce latency.
- **Web Interface**: Add a simple web front-end for easy access.

## Conclusion
This system efficiently combines OCR, text extraction, and hybrid search techniques to answer queries based on PDF content. It is designed to be scalable and extendable for future improvements.
