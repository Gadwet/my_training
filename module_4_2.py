def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()



test_function()
inner_function() # При вызове функции выдаёт ошибку, так как её нет в глобальном пространстве имён.