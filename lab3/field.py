def field(items, *args):
    assert len(args) > 0
    for x in items:
      for y in args:
        if y in x:
          print(x[y])
#goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
#]

#field(goods,'title', 'price','xc','dasd')