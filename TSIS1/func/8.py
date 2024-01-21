def myfunc():
    global x #глобальная сильнее поэтому она записывается последней
    x="amusing"
    print("Python is "+x)

myfunc()
print("Python is "+x)