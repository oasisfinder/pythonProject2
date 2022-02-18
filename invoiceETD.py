import os
a=""
b=""
c=""
d=""
e=""
f=""
g=""
h=""

a,b,c,d,e,f,g,h = input("인보이스 번호를 입력하세요 여러개는,로 구분").split(",")
os.system("booking.vbs {}{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g,h))

