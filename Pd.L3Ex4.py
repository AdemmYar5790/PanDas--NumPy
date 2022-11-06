In: authors_stat = authors_price['author_name'].value_counts()
print(authors_stat)

Out:
Тургенев      3
Островский    2
Чехов         2
Name: author_name, dtype: int64

In: authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
    authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)

Out:
                      price
               min_price   max_price  mean_price
author_name
Островский        290          370     330.000000
Тургенев          300          450     366.666667
Чехов             450          500     475.000000