# ✔ Вспомните какие модули вы уже проходили на курсе.
# ✔ Создайте файл, в котором вы импортируете встроенные
# в модуль функции под псевдонимами. (3-7 строк
# импорта).

import sys
from random import randint as rd
import math
from datetime import datetime as dt

print(sys.path)
for i in range(10):
    print(math.sqrt(rd(1, 10)))
print(dt.now())