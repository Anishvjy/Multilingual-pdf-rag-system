# Multilingual PDF RAG System

This project implements a **Retrieval-Augmented Generation (RAG)** system to process multilingual PDFs, extract text, and answer questions or generate summaries based on their content. It supports both scanned and digital PDFs, making it versatile and robust.

---

## Features
- **Multilingual Support**: Handles Hindi, English, Bengali, and Chinese.
- **Hybrid Search**: Combines semantic search (FAISS) with keyword search (BM25) for better retrieval accuracy.
- **Chat Memory**: Maintains context across multiple queries.
- **OCR Capability**: Extracts text from scanned PDFs using OCR techniques.
- **Scalable Design**: Handles large data volumes with efficient chunking and indexing.

---

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anishvjy/Multilingual-pdf-rag-system.git
   cd Multilingual-pdf-rag-system

2. **Install dependencies**: Make sure you have Python installed. Then, install the required packages using:
   pip install -r requirements.txt

3. **Run the main script**: Use the following command to run the system:
     python src/main.py

4. **Provide a query**: When prompted, enter a query related to the PDF content. The system will return a relevant answer.


## Folder Structure
Multilingual-pdf-rag-system/
├── src/                          # Source code files
│   ├── main.py                   # Main entry point of the application
│   ├── chat_memory.py            # Manages chat memory
│   ├── qa_pipeline.py            # QA model initialization and answering logic
│   ├── retrieval.py              # Retrieval functions and BM25 logic
│   ├── embedding_index.py        # Embedding and FAISS indexing logic
│   ├── chunking.py               # Text chunking algorithms
│   ├── preprocessing.py          # Preprocessing (cleaning and tokenization)
│   └── text_extraction.py        # Text extraction (OCR and digital)
├── data/                         # Folder for storing PDFs and extracted text
│   └── sample_pdfs/              # Sample PDFs for testing
├── docs/                         # Documentation files
│   ├── user_guide.md             # User guide for the project
│   └── system_architecture.md    # Technical documentation of system architecture
├── notebook/                     # Google Colab notebook of the full code
├── tests/                        # Unit tests for the project
├── setup.py                      # Script for setting up the project
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview and instructions

## Example Usage
query: "What is the main topic of the document?" (for a bengali pdf)
Answer:  অনাপি? সনদ

## Troubleshooting
**PDF not found**: Ensure the PDF paths are correct and the files are present in the data/sample_pdfs/ folder.
**Slow response**: Try with smaller PDFs or fewer documents for testing purposes.
**Dependencies error**: Make sure all required libraries are installed by running pip install -r requirements.txt.

## Future Improvements
Add a web-based interface for easier access.
Use smaller, more efficient language models to improve performance.
Implement query decomposition for complex questions.

## Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.

## Contact
For issues or support, contact the developer at:
Email: anishvijayvergiya1010@gmail.com

## License
This project is licensed under the MIT License.
