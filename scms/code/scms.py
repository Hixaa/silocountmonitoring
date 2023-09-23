import sys
from components.app import App
myapp = App()

try:
    myapp.run()
except:
    print("scms App exited safely!")
    sys.exit()
