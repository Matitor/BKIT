from contextlib import contextmanager
import time
@contextmanager
def cm_timer_1():
  start = time.monotonic()
  yield
  end = time.monotonic()
  print(end-start)
class cm_timer_2(object):
  def __enter__(self):
    cm_timer_2.start = time.monotonic()
  def __exit__(self, exc_type, exc_value, traceback):
    cm_timer_2.end = time.monotonic()
  def __del__(self):
    print(cm_timer_2.end-cm_timer_2.start) 
    
#with cm_timer_1():
#  time.sleep(1)
#with cm_timer_2():
#  time.sleep(1)