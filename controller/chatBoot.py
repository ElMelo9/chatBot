import nltk
import re
import random
import string
from string import punctuation
# Importar los patrones desde mis_patrones.py
from controller.mis_patrones import patrones


class Bot:
    def __init__(self):
        # Descargar los módulos de stopwords de nltk
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(nltk.corpus.stopwords.words('spanish'))

    def sentence_tokenizer(self, data):
        # Tokenización de oraciones
        return nltk.sent_tokenize(data.lower())

    def word_tokenizer(self, data):
        # Tokenización de palabras
        return nltk.word_tokenize(data.lower())

    def remove_noise(self, word_tokens):
        # Función para eliminar stop words y puntuación
        cleaned_tokens = []
        for token in word_tokens:
            if token not in self.stop_words and token not in punctuation:
                cleaned_tokens.append(token)
        return cleaned_tokens

    # Función para generar una respuesta para la entrada del usuario
    def generate_response(self, textCliente):
        # Tokenizar la entrada del usuario
        user_input_tokenized = self.word_tokenizer(textCliente)
        # Eliminar stop words
        user_input_nostops = self.remove_noise(user_input_tokenized)

        best_response = ""
        max_similarity = 0

        for pattern, responses in patrones:
            match = re.search(pattern, textCliente)
            if match:
                similarity = len(match.group()) / len(textCliente)
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_response = random.choice(responses)

        return best_response
