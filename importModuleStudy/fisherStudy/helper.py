

#判断是是ISBN检索还是 关键字检索
# isbn isbn13 -- 0-9个数字组成
# isbn10 -- 10个0-9个数字组成，含有一些' - '
def is_isbn_or_key(word):
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','') #去掉'-'判断是否是isbn10
    if len(word) == 10 and short_word.isdigit() and len(short_word)==10:
        isbn_or_key = 'isbn'
    return isbn_or_key

