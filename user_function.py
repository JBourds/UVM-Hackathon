def user_function(f:callable, x: list[int]):
	import numpy as np
	v_func = np.vectorize(f)
	result =(v_func(x))
	return result
