x="good"
def my():
    global x #глобальная сильнее поэтому она записывается последней
    x="THE BEST"
my()
print("PYTHON IS "+x)