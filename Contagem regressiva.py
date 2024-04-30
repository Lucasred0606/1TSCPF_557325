titulo = "Contagem Regressiva"
print(f"{titulo:^30}")

import time

for i in range(60, -1, -1):
    time.sleep(1)
    print(i)
