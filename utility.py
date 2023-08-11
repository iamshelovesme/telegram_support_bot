def read_text_message(path):
    f = open(path, "r", encoding="utf-8")
    text = f.read()
    f.close()
    return text