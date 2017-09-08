# encoding=utf-8
import sys
import jieba


fp = open("C:/Users/Ulysses/Desktop/train/1dicInTrain.txt", 'r')
dicRead = fp.read()
dicRead = dicRead.split()
dic = []
for word in dicRead:
    if word[0]!='\\':
        dic.append(word) #字典处理

fp = open("C:/Users/Ulysses/Desktop/dev/dev.txt", 'r')
dataIn = fp.read()
data = []
dots = ['\n','\n\n','，','。','？','！','、','（','）','：','“','”',' ','；','『','』','《','》','℃','…','～','＆','%','＋','－','×','÷','—']
string = ''
for d in dataIn:
    if d not in dots:
        string += d
    elif string!='':
        data.append(string)
        string = ''  #输入集合处理


def SplitWords(sentence,dic): #正向最大匹配
    splited =[]
    MAX_LEN = 6
    number = ''
    start = 0
    end = len(sentence)-1
    temp = min(MAX_LEN-1,end)
    while start <= end:
        point = temp
        while point >= start:
            if scentence[start:point+1] in dic:
                splited.append(scentence[start:point+1])
                p = len(scentence[start:point+1])
                break
            elif scentence[start:point+1] in ['０','１','２','３','４','５','６','７','８','９','．']:
                splited.append(scentence[start:point+1])
                p = len(scentence[start:point+1])
                break
            elif len(scentence[start:point+1]) == 1:
                splited.append(scentence[start:point+1])
                p = len(scentence[start:point+1])
                break
            else:
                point -= 1
                p = 1
        start += p
        if temp + p <= end:
            temp = temp + p
        else:
            temp = temp
    return splited

#写入文件
output = open("C:/Users/Ulysses/Desktop/1130310424-1130310325.txt","w+")

for scentence in data:
    result = SplitWords(scentence,dic)
    for out in result:
        output.write(out)
        output.write('\n')
    
output.close


    
    
    


