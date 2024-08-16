immutable_var = 25, 'age', 9.5
print(immutable_var)
# immutable_var[0] = 298 # Зачастую он используется в качестве хранилища, например, для какого-то списка, который мы ни коим образом не хотим трогать, то есть нам нужно чтобы он оставался неизменным.
mutable_list = [1, 'Hello', True]
mutable_list[1] = 'World'
print(mutable_list)