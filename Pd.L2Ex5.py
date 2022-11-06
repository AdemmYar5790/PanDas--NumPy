In: authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
print(authors_price)

Out:

author_id    author_name            book_title   price    cover
0          1    Тургенев           Отцы и дети    450    твердая
1          1    Тургенев                 Рудин    300    мягкая
2          1    Тургенев     Дворянское гнездо    350    мягкая
3          2       Чехов      Толстый и тонкий    500    твердая
4          2       Чехов       Дама с собачкой    450    твердая
5          3  Островский                 Гроза    370    мягкая
6          3  Островский  Таланты и поклонники    290    мягкая

In: book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
    book_info['мягкая'] = book_info['мягкая'].fillna(0)
    book_info['твердая'] = book_info['твердая'].fillna(0)
print(book_info)

Out:
cover        мягкая   твердая
author_name
Островский    660.0      0.0
Тургенев      650.0    450.0
Чехов           0.0    950.0

In: book_info.to_pickle('book_info.pkl')
Out:

In: book_info2 = pd.read_pickle('book_info.pkl')
Out:

In: book_info.equals(book_info2)

Out: True