
import auth
import auth_method
import error_window
from tkinter import *

if __name__ == '__main__':
    for service in auth_method.auth_method:
        root = auth.MainApp()
        result = root.generate_auth(service.inputs, service.name)


        print(result)
        while service.func_check(*result) is not True:
            error_window.MainApp()

            root = auth.MainApp()
            result = root.generate_auth(service.inputs, service.name)
            print(result)
