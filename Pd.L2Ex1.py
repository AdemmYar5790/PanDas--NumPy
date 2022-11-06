In: import pandas as pd
Out:

In: authors = pd.DataFrame({'author_id':[1, 2, 3],
                            'author_name':['Тургенев', 'Чехов', 'Островский']},
                             columns=['author_id', 'author_name'])
print(authors)
Out:
author_id  author_name
0          1    Тургенев
1          2       Чехов
2          3  Островский

In: book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                         'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                         'price':[450, 300, 350, 500, 450, 370, 290]},
                         columns=['author_id', 'book_title', 'price'])
print(book)
Out:
    author_id            book_title  price
0          1            Отцы и дети   450
1          1                  Рудин   300
2          1      Дворянское гнездо   350
3          2       Толстый и тонкий   500
4          2        Дама с собачкой   450
5          3                  Гроза   370
6          3   Таланты и поклонники   290

