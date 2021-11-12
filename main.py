def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()
        print("А я - код, срабатывающий после")
    return the_wrapper_around_the_original_function


@my_shiny_new_decorator
def printhi():
    print("Hello!")


if __name__ == '__main__':
    printhi()
