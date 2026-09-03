import streamlit as st
import requests
import json
import uuid

# 1. Setup Session State for memory and ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🚀 Enterprise RAG System")
st.sidebar.header("Document Upload")

# 2. Sidebar: File Upload to FastAPI
uploaded_file = st.sidebar.file_uploader("Upload a PDF or TXT", type=["pdf", "txt"])

if st.sidebar.button("Process Document"):
    if uploaded_file is not None:
        with st.spinner("Chunking and Vectorizing..."):
            # Prepare the file for the requests library
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            
            # Post to your FastAPI endpoint
            res = requests.post("http://127.0.0.1:8000/ai_chat/document/upload", files=files)
            
            if res.status_code == 200:
                st.sidebar.success(res.json().get("message"))
            else:
                st.sidebar.error(f"Upload failed: {res.text}")
    else:
        st.sidebar.warning("Please upload a file first.")

# 3. Main Chat Interface
# Display past messages in the UI
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new user input
if prompt := st.chat_input("Ask a question about your documents..."):
    # Show user question immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process AI Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        payload = {
            "session_id": st.session_state.session_id,
            "question": prompt,
            "top_k": 3
        }
        
        try:
            # 🔑 stream=True is critical to catch the NDJSON chunks as they arrive
            with requests.post("http://127.0.0.1:8000/ai_chat/rag/ask-stream", json=payload, stream=True) as r:
                for line in r.iter_lines():
                    if line:
                        data = json.loads(line.decode('utf-8'))
                        # Only grab the chunks that contain actual answer text
                        if "Answer Chunk" in data:
                            full_response += data["Answer Chunk"]
                            # Add a blinking cursor effect
                            message_placeholder.markdown(full_response + "▌")
                            
            # Remove cursor when finished
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
            
    # Save the final AI answer to Streamlit's memory so it persists on screen redraw
    st.session_state.messages.append({"role": "assistant", "content": full_response})