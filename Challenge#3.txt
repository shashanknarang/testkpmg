from functools import reduce
def deep_get(dictionary, keys, default=None):
	return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("/"), dictionary)

object = {"a1": { "b1": { "c1": "d1" }}}
object2 = {"x1":{"y1":{"z1":"a1"}}}
print (deep_get(object,"a1/b1/c1"))
print (deep_get(object2,"x1/y1/z1"))