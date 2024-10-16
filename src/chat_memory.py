# -*- coding: utf-8 -*-
"""chat_memory.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12x8xuZ3hNOhYkow-gutusxOO-tRZ7pEs
"""

# Chat memory to store previous interactions
chat_memory = []

def answer_query_with_memory(query, chunks, bm25):
    # Retrieve relevant chunks for the query
    relevant_chunks = get_top_k_chunks(query, chunks, bm25, k=5)

    print("Retrieved chunks:", relevant_chunks)  # Check retrieved chunks
    # Combine relevant chunks to create context
    context = " ".join(relevant_chunks)

    # Include chat history in the context
    if chat_memory:
        previous_interactions = " ".join([item['response'] for item in chat_memory])
        context = previous_interactions + " " + context

    # Store query and context in chat memory
    chat_memory.append({'query': query, 'context': context})

    # Get the answer from the QA model
    if context.strip():
        response = qa_model({'question': query, 'context': context})
        # Store the response in chat memory
        chat_memory.append({'response': response['answer']})
        return response['answer']
    else:
        return "I'm sorry, I couldn't find relevant information in the documents."