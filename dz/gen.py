def lazy_gen(goods):
  a,b=0,1
  for i in range(goods):
    yield a
    a,b=b,a+b