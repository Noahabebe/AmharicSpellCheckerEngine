# Artai Amharic Spell Checker

The Artai Amharic Spell Checker, an impactful creation by a team of SWE students at Addis Ababa Institute of Technology, addresses the unique challenges posed by Amharic as a low-resource language, catering to diverse linguistic backgrounds in Ethiopia. By providing a reliable solution for accurate spell checking, the tool becomes a valuable resource for individuals and companies facing spelling difficulties, contributing to enhanced communication and literacy. Beyond its immediate impact, this project has the potential to revolutionize the digital usage of Amharic, opening avenues for broader applications and advancements in various real-life projects that intersect with the rich linguistic diversity of Ethiopia.

## Project Overview
- **Campus**: Addis Ababa Institue of Technology.
- **Department**: Software and Information Technology Engineering
- **Course**: Fundamentals of Software Engineering I.
- **Advisor**: Instructor Nuniyat Kifle

### Team Members

1.	Abdulmunim Jundurahman      UGR/8625/14
2.	Bisrat Asaye                UGR/8508/14
3.	Ezana Kifle                 UGR/4189/14
4.	Fuad Mohammad               UGR/6052/14
5.	Sifan Fita                  UGR/8856/14
6.	Yordanos Zegeye             UGR/6316/14


## Key Features

- UltraFast Error Detection
- Context Aware Suggestion
- Part of Speech Tagging
- API Interface

## Getting Started

### Prerequisites

- Python 3.x
- Required dependencies (specified in `requirements.txt`)

### Installation

```bash
pip install -r requirements.txt
```

### Usage 
1. Clone this repository
```bash
git clone https://github.com/abdulmunimjemal/AmharicSpellCheckerEngine.git
cd AmharicSpellCheckerEngine
```
2. Run the spell checker
```bash
cd src
uvicorn main:app
```
## Project Structure

- **/**
  - `spell_checker.py`: Implementation of the `SpellChecker` class.
  - `spell_checker_pos.py`: Implementation of the `SpellChecker` class with Part of Speech Tagging.
  - `edit_distance.py`: Implementation of the Damerau-Levenshtein distance.
  - `ngram.py`: Implementation of N-gram model functions.
  - `train.ipynb`: Notebook for Training and usage of a bigram language model on the corpus for suggestion ranking.
  - `file_reader.py`: Implementation of file reading functions.
  - `tokenizer.py`: Implementation of an Amharic tokenizer.
  - `normalizer.py`: Implementation of an Amharic normalizer.
  - `dictionary.py`: Implementation of a Dictionary Class with O(1) Time Complexity and O(n) Space Complexity for Word Lookup.
  - `main.py`: Main script for running the spell checker API.
  - `utils.py`: Implementation of Utility Functions.
  - `preprocessing.py`: Implementation of Amahric text preprocessing functions.
  - **models/**
     - `am_pos_model.pt`: Amharic Part of Speech Tagger Model
     - `bigram_model.pt`: Amharic Bigram Model
     - `trigram_model.pt`: Amharic Trigram Model
  - **tests/**
    - `test_edit_distance.py`: Unit Test Edit Distance Algorithm
    - `test_normalizer.py`: Unit Test Amharic Normalizer
    - `test_preprocessing.py`: Integration Test Preprocessing Pipeline
    - `test_spell_checker.py`: End to End Test Spell Checker Engine with AP
    
  - **data/**
    - `amharic_dictionary*.txt`: Dictionary files with Amharic words.
    - `amharic_corpus.txt`: Corpus file with Amharic sentences.

### Documentation

  - `LICENSE`: Project license file.
  - `requirements.txt`: List of project dependencies.
  - `README.md`: Project documentation.
