def f(w, a, b):
    w.append(a)
    print(id(w))
    w = w + [b]
    print(id(w))
    return w


w, a, b = [5, 9], 2, 1
print(id(w))
w = f(w, a, b) + w
print(w)

[5, 9, 2, 1, 5, 9, 2]