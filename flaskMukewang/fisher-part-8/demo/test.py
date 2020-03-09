a = "a"
b = "b"
c = "c"

intros = filter(lambda x: True if x else False, [a, b, c])
print(type(intros),intros)
print('/'.join(intros))