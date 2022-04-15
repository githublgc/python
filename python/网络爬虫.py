from urllib import request
url='https://www.nankai.edu.cn/'
content=request.urlopen(url).read()
print(content)
