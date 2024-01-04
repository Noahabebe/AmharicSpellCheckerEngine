import re, string
from typing import List
from utils import apply_rules, RULES

# TODO: HANDLE COMPOUND WORDS SUCH AS ስነ

class AmharicSegmenter:
    def __init__(self, word_delimiters: set = None, sentence_delimiters: set = None):
        """
        :param word_delimiters (optional): word delimiters to use for tokenization (default: whitespace + punctuations)
        :param sentence_delimiters (optional): sentence delimiters to use for tokenization (default: "።", "፥", "፨", "::", "፡፡", "?", "!",'፧')
        :param include_punc: Include punctuations in the word tokens.
        :param compound_words_as_one: Include compounds words in the word tokens as one word.
                
        :return: a list of word-tokenized sentences
        
        Amharic Tokenizer for tokenization and sentence segmentation.

        Args:
        -  (Set[str]): List of sentence-ending punctuations.
        - word_punctuations (Set[str]): List of word-ending punctuations.
        """
        self.__word_delimiters = word_delimiters or { "[", " ", "፣", "።", ",", "፦", "!", ">", "&", "፧", "}", "^", ")", "፨", "<", "~", "]", "*", "{", "፤", "/", "፥", "(", "\\", "_", "+", ";", "#", "\"", ":", "=", " ", "%", "|", "`", "@", "'", "?", "$", }
        self.__sentence_delimiters = sentence_delimiters or ["።", "፥", "፨", "::", "፡፡", "?", "!",'፧']
        self.__compound_words_fix = [
            'ስነ','ቤተ', 'እግረ','ሥነ'
        ]

    def word_tokenize(self, text: str, include_punc=False, compound_words_as_one=True):
        """
        Tokenize a text into a list of tokens.

        :param text: the text to tokenize
        :param include_punc: include punctuation in the tokens
        :return: a list of tokens
        """

        delimiters = self.__word_delimiters
        compound_words = self.__compound_words_fix
        
        tokens = []
        curr_word = ""
        prev_word = None
        
        for char in text:
            if char not in delimiters:
                curr_word += char
            else:
                curr_word = curr_word.strip()
                if curr_word:
                    if compound_words_as_one and curr_word in self.__compound_words_fix:
                        continue
                    tokens.append(curr_word)
                    prev_word = curr_word
                    if include_punc and char != ' ': tokens.append(char);prev_word = char;
                    curr_word = ""
                
                
        if curr_word.strip(): # if a word exists and is not whitespace
            tokens.append(curr_word.strip())
        return tokens

    def sentence_tokenize(self, text: str):
        """
        Tokenize a text into a list of sentences.

        :param text: the text to tokenize
        :return: a list of sentences
        """

        sentences = []
        current_sentence = ""
    
        for char in sentences:
            if char not in self.__sentence_delimiters:
                current_sentence += char
            elif current_sentence.strip():
                sentences.append(current_sentence.strip())
                current_sentence = ""

        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        return sentences

    def matrix_tokenize(self, text: str, include_punc=False, compound_words_as_one=False) -> List[List[str]]:
        """
        Tokenize text in to list of tokenized sentences.
        
        :param text: the text to tokenize
        :param include_punc: Include punctuations in the word tokens.
        :param compound_words_as_one: Include compounds words in the word tokens as one word.
                
        :return: a list of word-tokenized sentences
        """

        matrix = []
        curr_row = []
        curr_word = ""
        prev_word = None
        
        for char in text:
            if char not in self.__sentence_delimiters and char not in self.__word_delimiters:
                curr_word += char
            elif char in self.__word_delimiters:
                curr_word = curr_word.strip()
                if curr_word:
                    if compound_words_as_one and curr_word in self.__compound_words_fix:
                        continue
                    curr_row.append(curr_word)
                    prev_word = curr_word
                    if include_punc and char != ' ': tokens.append(char);prev_word = char;
                    curr_word = ""
                if char in self.sentence_delimiters:
                    matrix.append(curr_row)
                    curr_row = []
                    
                    
        if current_word.strip(): curr_row.append(current_word.strip())
        if current_row: matrix.append(current_row)

        return matrix