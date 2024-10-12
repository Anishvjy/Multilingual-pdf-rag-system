# User Guide for Multilingual PDF RAG System

## Introduction
This system is designed to process multilingual PDFs (Hindi, English, Bengali, Chinese) and provide answers or summaries based on the content. It can handle both scanned and digital PDFs.

## How to Use
1. **Install Dependencies**: 
   Use the following command to install the necessary libraries:
   ```bash
   pip install -r requirements.txt

2. **Run the Application**: Run the main script by executing:
    python src/main.py

3. **Enter a Query**: After the script runs, you will be prompted to enter your query. The system will return a relevant answer based on the PDF contents.

## Features
**Language Detection**: Automatically detects the language of extracted text.
**Hybrid Search**: Combines semantic search using FAISS and keyword search using BM25.
**Chat Memory**: Maintains chat context across queries.

## Troubleshooting
**PDF not found**: Ensure that your PDF path is correct and accessible.
**Slow response**: Large PDFs may take longer to process; try with smaller PDFs for quicker testing.

## Contact
For issues or support, contact the developer at:
Email: anishvijayvergiya1010@gmail.com