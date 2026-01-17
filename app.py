import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

@st.cache_resource
def load_resources():
    model = load_model('sherlock.keras')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return model, tokenizer

model, tokenizer = load_resources()

st.title("Sherlock Holmes Story Generator")
st.write("Generate Sherlock Holmes stories based on your input prompt.")

seed_text = st.text_area(
    "Enter Starting words for the story:",
    value="", 
    placeholder="e.g., Sherlock Holmes said"
)

next_words = st.slider("Number of words to generate:", min_value=10, max_value=120, value=20)

# Text generation
if st.button("Generate Story"):
    max_len = 20
    generated_text = seed_text
    progress_bar = st.progress(0)

    for i in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_len, padding='pre')
        predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)

        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
        generated_text += " " + output_word

        progress_bar.progress((i + 1) / next_words)

    st.success("Here is your story:")
    st.write(generated_text)

# Footer with author and model info
st.markdown("---")
st.markdown(
    "👤 **Author:** Mehedi Hasan  \n"
    "🧠 **Model:** LSTM (Long Short-Term Memory) trained on Sherlock Holmes stories"
)
