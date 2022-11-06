In: top5 = authors_price.nlargest(5, 'price')
print(top5)

Out:
author_id    author_name         book_title   price
3          2       Чехов   Толстый и тонкий    500
0          1    Тургенев        Отцы и дети    450
4          2       Чехов    Дама с собачкой    450
5          3  Островский              Гроза    370
2          1    Тургенев  Дворянское гнездо    350