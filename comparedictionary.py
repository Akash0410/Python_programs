from multiprocessing.sharedctypes import Value
from webbrowser import get


a={'l':90,'m':85,'n':100,'o':60}
print(max(a.values()))
for key,value in a.items():
    if (max(a.values())==value):
        print(key)
    