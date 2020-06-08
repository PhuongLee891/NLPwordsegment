mydict=[]
Input = "Những hướng dẫn viên du lịch trong thời kỳ dịch bệnh này đang không thể đi làm."

def getMydict():
    f = open('VDic_uni.txt', 'rt', encoding= 'utf-8')
    for i in f:
        i = i.replace('\ufeff','')              #delete '\ufeff'
        i = i.lower()
        i = i[0:i.find('\t')]                   #get keyword
        mydict.append(i)

#Run here
getMydict()
Input = Input.lower()
Input = Input.strip()
if Input[-1] in ['.',',',':','!','?']:
    Input = Input[:-1] + " " + Input[-1]
listword = Input.split(' ')


lengthW = 0                                     #Độ dài word hiện tại
temp = 0
point = 0                                       #Con trỏ
Output = []
while point < len(listword):
    myword = ''
    for i in range(0,4):                        #Xét từ có 1 đến 4 hình vị.
        if point + i > len(listword) -1:
            continue
        myword = myword + ' ' + listword[point + i]
        myword = myword.strip()
        if myword in mydict:
            temp = i                            #Độ dài từ hợp lý (Nếu không có từ hợp lý mặc định là 0)
    word = ''
    for i in range(point,point+temp+1):         #Thêm vào Output từ hợp lý đã tách ở trên
        word = word + ' ' + listword[i]
    word = word.strip()
    Output.append(word)
    point = point + temp + 1
print(Output)
            