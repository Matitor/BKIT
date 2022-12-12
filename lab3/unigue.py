class Unique(object):
    def __init__(self, items, **kwargs):
      self.i=[]
      for key, value in kwargs.items():
        if key == 'ignore_case' and value == True:
          items =[j.lower() for j in items]
      for j in items:
        if j not in self.i:
          self.i.append(j)
        
    def __next__(self):
      try:
        x = self.i[self.begin]
        self.begin += 1
        return x
      except:
        raise StopIteration

    def __iter__(self):
      self.begin = 0
      return self

#data = ['a', 'A', 'b', 'B', 'a', 'A','b', 'B']
#for i in Unique(data,ignore_case=True):
#  print(i)