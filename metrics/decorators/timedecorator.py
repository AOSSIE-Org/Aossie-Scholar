def my_timer(func):
	import time

	def wrapper(*args, **kwargs):
		t1=time.time()
		result=func(*args, **kwargs)
		t2=time.time()-t1
		print ('{} ran in: {} sec'.format(func.__name__,t2))
		return result
	return wrapper