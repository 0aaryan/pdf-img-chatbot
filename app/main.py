import streamlit as st
from pdf_img_chatbot.chatbot import ChatBot
import os
import tempfile

# title and page config
st.set_page_config(page_title="PDF AND IMAGE CHATBOT", page_icon="🤖")

def init():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "qdrant_db" not in st.session_state:
        st.session_state.qdrant_db = None
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBot()
    if "file" not in st.session_state:
        st.session_state.file = None
    if "temp_dir" not in st.session_state:
        st.session_state.temp_dir = None
    if "img_file" not in st.session_state:
        st.session_state.img_file = None
    if "image_description" not in st.session_state:
        st.session_state.image_description = None

# sidebar
def upload_file():
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])
    if st.button("Upload and chat"):
        if uploaded_file is not None:
            # save file
            st.session_state.file = uploaded_file
            st.session_state.temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(st.session_state.temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.session_state.chatbot.upload_file(file_path)
            st.success("File uploaded successfully")
        else:
            st.warning("Please upload a file")

    if st.button("Clear chat"):
        st.session_state.chat_history = []
        st.session_state.img_file = None
        st.session_state.image_description = None
        st.success("Chat cleared")

    image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        st.session_state.img_file = image_file
        st.image(image_file, caption="Uploaded Image", use_column_width=True)
        image_description = st.session_state.chatbot.get_image_description(image_file)
        st.session_state.image_description = image_description
        st.write(f"Image description: {image_description}")
        st.success("Image uploaded successfully")

def chatbot():

    for chat in st.session_state.chat_history:
        st.chat_message(chat["role"]).markdown(chat["message"])
    

    user_input = st.chat_input("Ask anything about your file")
    if user_input:
        if st.session_state.file is None:
            st.warning("Please upload a file first")
            return
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "message": user_input})
        with st.spinner("Thinking..."):
            chat_history_str = "\n".join([chat["message"] for chat in st.session_state.chat_history[-5:]])
            content = st.session_state.chatbot.get_content(user_input)
            with st.expander("Show content"):
                st.write(content)
            if st.session_state.img_file is not None:
                content += f"\nImage description: {st.session_state.image_description}"
            response = st.session_state.chatbot.chat(user_input, chat_history_str, content)
            st.chat_message("bot").markdown(response)
            st.session_state.chat_history.append({"role": "bot", "message": response})




def main():
    init()
    st.title("PDF AND IMAGE CHATBOT")
    with st.sidebar:
        st.subheader("Upload File")
        upload_file()
    chatbot()

if __name__ == "__main__":
    main()