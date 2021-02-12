def my_generator():
    received = yield 1
    print(f'??? = {received}')

it = iter(my_generator())
output = it.send(it)     # ? ?? ????? ??? ???
print(f'??: {output}')

try:
    it.send('??!')    # ?? ?????? ???
except TypeError:
    pass
