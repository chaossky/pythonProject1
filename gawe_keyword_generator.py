file=open('list001.txt','w')
str01="강남구,강동구,강북구,강서구,관악구,광진구,구로구,금천구,노원구,도봉구,동대문구,동작구,마포구,서대문구,서초구,성동구,성북구,송파구,양천구,영등포구,용산구,은평구,종로구,중구,중랑구"
to=str01.split(',')

for i in range(len(to)):
    print(to[i])
for i in range(len(to)):
    file.writelines(to[i]+"과외 \n")
for i in range(len(to)):
    file.writelines(to[i]+"개인과외 \n")
for i in range(len(to)):
    file.writelines(to[i]+"영어과외 \n")
for i in range(len(to)):
    file.writelines(to[i]+"수학과외 \n")


file.close()