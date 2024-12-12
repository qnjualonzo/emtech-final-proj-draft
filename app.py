import streamlit as st
from transformers import pipeline

# Set up the Streamlit app
def main():
    st.title("Translation App")
    st.write("This app uses a pre-trained transformer model to translate text between languages.")

    # Sidebar options
    st.sidebar.title("Translation Settings")
    source_lang = st.sidebar.selectbox(
        "Select source language:",
        ["en", "fr", "de", "es", "it"]  # Add other supported languages as needed
    )
    target_lang = st.sidebar.selectbox(
        "Select target language:",
        ["en", "fr", "de", "es", "it"]
    )

    if source_lang == target_lang:
        st.sidebar.warning("Source and target languages should be different.")

    # Text input for translation
    text_to_translate = st.text_area("Enter the text you want to translate:", "")

    if st.button("Translate"):
        if not text_to_translate.strip():
            st.error("Please enter text to translate.")
        else:
            with st.spinner("Translating..."):
                try:
                    # Load translation pipeline
                    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
                    translator = pipeline("translation", model=model_name)

                    # Perform translation
                    translation = translator(text_to_translate, max_length=400)[0]['translation_text']

                    # Display result
                    st.success("Translation completed!")
                    st.text_area("Translated text:", translation, height=150)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
