In: authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)

Out:
author_id   author_name            book_title   price
0          1    Тургенев           Отцы и дети    450
1          1    Тургенев                 Рудин    300
2          1    Тургенев     Дворянское гнездо    350
3          2       Чехов      Толстый и тонкий    500
4          2       Чехов       Дама с собачкой    450
5          3  Островский                 Гроза    370
6          3  Островский  Таланты и поклонники    290