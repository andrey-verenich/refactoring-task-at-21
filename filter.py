from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for nikel in range(j, j + 10):
                n1 = arr[n][nikel][0] // 3
                n2 = arr[n][nikel][1] // 3
                n3 = arr[n][nikel][2] // 3
                M = n1 + n2 + n3
                s += M
        s = s // 100
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = s
                arr[n][n1][1] = s
                arr[n][n1][2] = s
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
