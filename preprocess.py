import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')


def preprocess(words):
    words = words.lower()
    words = words.split()
    words = [word.strip('.,!;()[]:?{}-') for word in words]
    words = [word.replace("'s", '') for word in words if word not in stop_words]
    # words = [word for word in words if word not in stop_words]
    return words
