from pathlib import Path

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer  # activated -> deactivate
# from nltk.stem import WordNetLemmatizer # deactivated -> activate

from src.main.py.const import Const


class Processor:
    """Class containing methods for text processing"""

    @staticmethod
    def preprocess(doc):
        """Cleans up document"""

        stemmer = PorterStemmer()
        doc_clean = doc.lower()
        doc_clean = word_tokenize(doc_clean)
        doc_clean = [word for word in doc_clean if word not in stopwords.words('english')]
        doc_clean = [word for word in doc_clean if word.isalpha()]
        doc_clean = [stemmer.stem(word) for word in doc_clean]  # or lemmatizer.lemmatize(word)
        return doc_clean

    @staticmethod
    def mediocrity_index(doc):
        """Calculates mediocrity index"""

        doc_clean = Processor.preprocess(doc)
        total_words = len(doc_clean)
        unique_words = len(set(doc_clean))
        return float(unique_words) / total_words  # if you use casting, then something is wrong (:

    @staticmethod
    def score(doc1, doc2):
        """Calculates score of doc2, assuming that doc1 is reference measuring system (it's score = 1)"""
        return Processor.mediocrity_index(doc1) / Processor.mediocrity_index(doc2)


if __name__ == '__main__':
    war_and_peace = Path(Const.WAR_TEXT).read_text()
    print(war_and_peace)

    war_and_peace2 = Processor.preprocess(war_and_peace)
    print(war_and_peace2)

    Path('B1CH1_clean.txt').write_text(' '.join(war_and_peace2))

    readme = Path(Const.README).read_text()
    print(readme)

    print(Processor.score(war_and_peace, readme))
    print(Processor.score(war_and_peace, war_and_peace))
