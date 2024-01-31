import streamlit as st
import time

from spell_checker import SpellChecker
from spell_checker_pos import SpellCheckerWithPOS
from dictionary import Dictionary
from ngram import NgramModel

def load_models():
    dictionary_path = "data/amharic_dictionary_v1.txt"
    bigram_model_path = "models/bigram_model.pkl"
    trigram_model_path = "models/trigram_model.pkl"
    pos = "models/am_pos_model.pt"

    st.write("Loading models...")
    t1 = time.time()
    dictionary_model = Dictionary(dictionary_path)
    ngram_model = NgramModel.load(bigram_model_path)

    spell_checker = SpellChecker(dictionary_model, ngram_model)
    spell_checker_pos = SpellCheckerWithPOS(dictionary_model, ngram_model, pos)
    st.write(f"Models loaded successfully in {round(time.time() - t1, 3)} seconds")

    return spell_checker, spell_checker_pos

def main():
    st.title("Amharic Spell Checker")

    spell_checker, spell_checker_pos = load_models()

    option = st.selectbox("Select Spell Checker Type", ["Basic Spell Checker", "Advanced Spell Checker"])

    text = st.text_area("Enter the text you want to spellcheck")

    if st.button("Check Spelling"):
        if option == "Basic Spell Checker":
            result = spell_checker.check(text)
        else:
            result = spell_checker_pos.check(text)

        st.write("Spellchecking Result:")
        st.write(result)

if __name__ == "__main__":
    main()
