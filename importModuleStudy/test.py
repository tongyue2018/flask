

def is_isbn_or_key_test(word):
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','') #去掉'-'判断是否是isbn10
    if len(word) == 10 and short_word.isdigit() and len(short_word)==10:
        isbn_or_key = 'isbn'
    return isbn_or_key
