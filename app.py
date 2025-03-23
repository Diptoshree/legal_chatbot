# import streamlit as st
# import fitz  # PyMuPDF
# import google.generativeai as genai

# # Configure Gemini API key
# API_KEY = "AIzaSyAymA7P4sRcrb0S9IAsC2cgkfxc0a6Fzj8"
# genai.configure(api_key=API_KEY)

# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_file):
#     """Extracts text from an uploaded PDF file."""
#     doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
#     text = "\n".join(page.get_text("text") for page in doc)
#     return text[:30000]  # Limiting text to avoid exceeding model limits

# # Function to ask Gemini a question
# def ask_gemini(document_text, question):
#     """Sends the extracted text and question to Gemini API."""
#     prompt = f"""
#     You are an AI legal assistant. Based on the following legal document, answer the question in 100-200 words. 
#     The answer should be from the document only.
    
#     LEGAL DOCUMENT:
#     {document_text}
    
#     QUESTION: {question}
#     """
    
#     model = genai.GenerativeModel("gemini-2.0-flash")
#     response = model.generate_content(prompt)
#     return response.text if response else "No response from the model."

# # Streamlit UI
# st.title("Legal Document Q&A Chatbot")

# # File uploader
# uploaded_file = st.file_uploader("Upload a legal PDF document", type=["pdf"])

# document_text = ""
# if uploaded_file:
#     with st.spinner("Extracting text from document..."):
#         document_text = extract_text_from_pdf(uploaded_file)
#     st.success("Text extracted successfully!")

# # Question input
# question = st.text_input("Ask a question about the document:")

# # Submit button
# if st.button("Get Answer") and document_text and question:
#     with st.spinner("Fetching answer from AI..."):
#         answer = ask_gemini(document_text, question)
#     st.subheader("Answer:")
#     st.write(answer)
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

# Configure Gemini API key
API_KEY = "AIzaSyAymA7P4sRcrb0S9IAsC2cgkfxc0a6Fzj8"
genai.configure(api_key=API_KEY)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join(page.get_text("text") for page in doc)
    return text[:150000]  # Limiting text to avoid exceeding model limits

# Function to generate summary
def generate_summary(document_text):
    """Generates a 300-word summary of the legal document."""
    prompt = f"""
    You are an AI legal assistant. Summarize the following legal document in 300 words, preserving key facts and legal context.
    
    LEGAL DOCUMENT:
    {document_text}
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response else "No response from the model."

# Function to extract key legal points
def extract_key_points(document_text):
    """Extracts 5 key legal points in Q&A format from the document."""
    prompt = f"""
    You are an AI legal assistant. Extract 5 key legal points from the following document in question-and-answer format. 
    Each answer should be 1-2 lines long.
    
    LEGAL DOCUMENT:
    {document_text}
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response else "No response from the model."

# Function to ask Gemini a question
def ask_gemini(document_text, question):
    """Sends the extracted text and question to Gemini API."""
    prompt = f"""
    You are an AI legal assistant. Based on the following legal document, answer the question in 100-200 words. 
    The answer should be from the document only.
    
    LEGAL DOCUMENT:
    {document_text}
    
    QUESTION: {question}
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response else "No response from the model."

# Streamlit UI
st.title("Legal Intelligent Chatbot")

# File uploader
uploaded_file = st.file_uploader("Upload a legal PDF document", type=["pdf"])

document_text = ""
if uploaded_file:
    with st.spinner("Extracting text from document..."):
        document_text = extract_text_from_pdf(uploaded_file)
    st.success("Text extracted successfully!")

# Output options
if document_text:
    option = st.radio("Choose an option:", ("Summary", "Key Legal Points", "Ask a Question"))
    
    if option == "Summary":
        with st.spinner("Generating summary..."):
            summary = generate_summary(document_text)
        st.subheader("Summary:")
        st.write(summary)
    
    elif option == "Key Legal Points":
        with st.spinner("Extracting key legal points..."):
            key_points = extract_key_points(document_text)
        st.subheader("Key Legal Points:")
        st.write(key_points)
    
    elif option == "Ask a Question":
        question = st.text_input("Enter your question:")
        if st.button("Get Answer") and question:
            with st.spinner("Fetching answer from AI..."):
                answer = ask_gemini(document_text, question)
            st.subheader("Answer:")
            st.write(answer)
