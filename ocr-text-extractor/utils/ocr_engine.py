import easyocr

def load_reader(lang="en", gpu=False):
    langs = [lang, "en"] if lang != "en" else ["en"]
    return easyocr.Reader(langs, gpu=gpu)