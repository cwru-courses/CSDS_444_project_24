class des():

    def __init__(self):
        self.IPT=[
          58, 50, 42, 34, 26, 18, 10,  2,
          60, 52, 44, 36, 28, 20, 12,  4,
          62, 54, 46, 38, 30, 22, 14,  6,
          64, 56, 48, 40, 32, 24, 16,  8,
          57, 49, 41, 33, 25, 17,  9,  1,
          59, 51, 43, 35, 27, 19, 11,  3,
          61, 53, 45, 37, 29, 21, 13,  5,
          63, 55, 47, 39, 31, 23, 15,  7
        ]

        self.Inverse_IP_table = [
          40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21,  61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11,  51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41,  9,   49, 17, 57, 25
        ]

        self.Enlarge_table = [
          32, 1,  2,  3,  4,  5,
          4,  5,  6,  7,  8,  9,
          8,  9,  10, 11, 12, 13,
          12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21,
          20, 21, 22, 23, 24, 25,
          24, 25, 26, 27, 28, 29,
          28, 29, 30, 31, 32, 1
        ]

        self.Key_table = [
          57, 49, 41, 33, 25, 17, 9,
          1,  58, 50, 42, 34, 26, 18,
          10, 2,  59, 51, 43, 35, 27,
          19, 11, 3,  60, 52, 44, 36,
          63, 55, 47, 39, 31, 23, 15,
          7,  62, 54, 46, 38, 30, 22,
          14, 6,  61, 53, 45, 37, 29,
          21, 13, 5,  28, 20, 12, 4
        ]

        self.Shrink_key_table = [
          14, 17, 11, 24, 1,  5,
          3,  28, 15, 6,  21, 10,
          23, 19, 12,  4, 26, 8,
          16, 7,  27, 20, 13, 2,
          41, 52, 31, 37, 47, 55,
          30, 40, 51, 45, 33, 48,
          44, 49, 39, 56, 34, 53,
          46, 42, 50, 36, 29, 32
        ]

        self.S1 = [
          14, 4,  13, 1,  2,   15, 11,  8,  3,   10,  6,  12, 5,  9,  0,  7,
          0,  15, 7,  4,  14,  2,  13,  1,  10,  6,   12, 11, 9,  5,  3,  8,
          4,  1,  14, 8,  13,  6,  2,   11, 15,  12,  9,  7,  3,  10, 5,  0,
          15, 12, 8,  2,  4,   9,  1,   7,  5,   11,  3,  14, 10, 0,  6,  13
        ]

        self.S2 = [
          15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13,  12,  0,  5,   10,
          3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10,  6,   9,  11,  5,
          0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12,  6,  9,   3,  2,   15,
          13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12,  0,   5,  14,  9
        ]

        self.S3 = [
          10,  0,  9,  14,  6,  3,  15,  5,   1,   13, 12,  7,   11,  4,  2,   8,
          13,  7,  0,  9,   3,  4,  6,   10,  2,   8,  5,   4,   12,  11, 15,  1,
          13,  6,  4,  9,   8,  15, 3,   0,   11,  1,  2,   12,  5,   10, 14,  7,
          1,   10, 13, 0,   6,  9,  8,   7,   4,   15, 14,  3,   11,  5,  2,   12
        ]

        self.S4 = [
          7,   13,  14,  3,  0,   6,   9,   10,  1,   2,  8,  5,   11, 12,  4,   15,
          13,  8,   11,  5,  6,   15,  0,   3,   4,   7,  2,  12,  1,  10,  14,  9,
          10,  6,   9,   0,  12,  11,  7,   13,  15,  1,  3,  14,  5,  2,   8,   4,
          3,   15,  0,   6,  10,  1,   13,  8,   9,   4,  5,  11,  12, 7,   2,   14
        ]

        self.S5 = [
          2,  12,  4,   1,   7,  10,  11,  6,   8,   5,   3,   15,  13,  0,  14,  9,
          14, 11,  2,   12,  4,  7,   13,  1,   5,   0,   15,  10,  3,   9,  8,   6,
          4,  2,   1,   11,  10, 13,  7,   8,   15,  9,   12,  5,   6,   3,  0,   14,
          11, 8,   12,  7,   1,  14,  2,   13,  6,   15,  0,   9,   10,  4,  5,   3
        ]

        self.S6 = [
          12,  1,   10,  15,  9,  2,   6,   8,  0,  13,  3,  4,   14,  7,   5,   11,
          10,  15,  4,   2,   7,  12,  9,   5,  6,  1,   13, 14,  0,   11,  3,   8,
          9,   14,  15,  5,   2,  8,   12,  3,  7,  0,   4,  10,  1,   13,  11,  6,
          4,   3,   2,   12,  9,  5,   15,  10, 11, 14,  1,  7,   6,   0,   8,   13
        ]

        self.S7 = [
          4,   11,  2,   14, 15,  0,  8,   13,  3,   12,  9,  7,   5,   10,  6,  1,
          13,  0,   11,  7,  4,   9,  1,   10,  14,  3,   5,  12,  2,   15,  8,  6,
          1,   4,   11,  13, 12,  3,  7,   14,  10,  15,  6,  8,   0,   5,   9,  2,
          6,   11,  13,  8,  1,   4,  10,  7,   9,   5,   0,  15,  14,  2,   3,  12
        ]

        self.S8 = [
          13,  2,   8,   4,  6,   15,  11,  1,  10,  9,   3,  14,  5,   0,   12,  7,
          1,   15,  13,  8,  10,  3,   7,   4,  12,  5,   6,  11,  0,   14,  9,   2,
          7,   11,  4,   1,  9,   12,  14,  2,  0,   6,   10, 13,  15,  3,   5,   8,
          2,   1,   14,  7,  4,   10,  8,   13, 15,  12,  9,  0,   3,   5,   6,   11
        ]

        
        self.P_table=[
            16, 7,  20, 21,
            29, 12, 28, 17,
            1,  15, 23, 26,
            5,  18, 31, 10,
            2,  8,  24, 14,
            32, 27, 3,  9,
            19, 13, 30, 6,
            22, 11, 4,  25
        ]

        self.Remove_key = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

        self.S = [self.S1,self.S2,self.S3,self.S4,self.S5,self.S6,self.S7,self.S8]


        self.key = []
        self.tempFile = []
        self.path = []
        self.file = []
        self.progress = 0

    def processKey(self,key):
        key = list(key)
        sortKey = []
        for num in self.Key_table:
            sortKey.append(key[num-1])
        leftKey = sortKey[0:28]
        rightKey = sortKey[28:56]
        resultKey = []
        for num in self.Remove_key:
            tempLeft = leftKey[num:len(leftKey)]
            tempRight = rightKey[num:len(rightKey)]
            if num==1:
                tempLeft.append(leftKey[0])
                tempRight.append(rightKey[0])
            else:
                tempLeft.append(leftKey[0])
                tempLeft.append(leftKey[1])
                tempRight.append(rightKey[0])
                tempRight.append(rightKey[1])
            leftKey = tempLeft
            rightKey = tempRight
            tempKey = tempLeft+tempRight
            result = ""
            for num in self.Shrink_key_table:
                result = result+tempKey[num-1]
            resultKey.append(result)
        return resultKey


    def processMessage(self,code,keyList,type):
        code = list(code)
        inverseCode = []
        for num in self.IPT:
            inverseCode.append(code[num-1])
        code = inverseCode
        left = code[0:32]
        right = code[32:64]
        index=0
        while index!=16:
            enlargeRight = []
            for num in self.Enlarge_table:
                enlargeRight.append(int(right[num-1]))
            value = 0
            if type==0:
                value = index
            elif type==1:
                value = 15-index
            tempKey = keyList[value]
            tempKey = list(tempKey)
            i=0
            tempResult = []
            while i!=48:
                if int(enlargeRight[i])==int(tempKey[i]):
                    tempResult.append(0)
                else:
                    tempResult.append(1)
                i+=1
            i=0
            sResult = ""
            while i!=8:
                tempS = tempResult[i*6:i*6+6]
                X = str(tempS[0])+str(tempS[5])
                Y = tempS[1:5]
                yaxis = ""
                for element in Y:
                    yaxis = yaxis+str(element)
                X = int(X,2)
                Y = int(yaxis,2)
                position = X*16+Y
                num = self.S[i][position]
                num = bin(num)
                num = str(num)
                num = num[2:len(num)]
                if len(num)==1:
                    num = "000"+num
                elif len(num)==2:
                    num = "00"+num
                elif len(num)==3:
                    num = "0"+num
                sResult = sResult+str(num)
                i+=1
            tempP = []
            sResult = list(sResult)
            for element in self.P_table:
                tempP.append(sResult[element-1])
            tempRight = right
            right = []
            i=0
            while i!=32:
                if int(left[i])==int(tempP[i]):
                    right.append(0)
                else:
                    right.append(1)
                i+=1
            left = tempRight
            index+=1
        tempFinalResult = right+left
        finalResult = ""
        for num in self.Inverse_IP_table:
            finalResult = finalResult+str(tempFinalResult[num-1])
        return  finalResult


    def processBinMessage(self,binMessage,key,type):
        listBinMessage = []
        i = len(binMessage)/64
        i = int(i)
        index = 0
        while index!=i:
            info = binMessage[index*64:index*64+64]
            listBinMessage.append(info)
            index+=1
        result = ""
        keyList = self.processKey(key)
        num = 0
        for code in listBinMessage:
            temp = self.processMessage(code,keyList,type)
            result = result+temp
            num+=1
            self.progress = num/len(listBinMessage)*100
        return result

    def toBin(self,message):
        byteMessage = ""
        for element in message:
            byte = ""
            try:
                element.encode("ascii")
                byte = ord(element)
                byte = bin(byte)
                byte = byte[2:len(byte)]
                while len(byte)<8:
                    byte = "0"+byte
            except:
                byte = bytes(element,encoding="utf-8")
                if len(byte) == 2:
                    byte= str(byte)
                    byte = byte.split("x")
                    byte = byte[1:len(byte)]
                    byte[0] = byte[0][0:2]
                    byte[1] = byte[1][0:2]
                    newByte = ""
                    for element in byte:
                        element = bin(int(element, 16))
                        element = element[2:len(element)]
                        while len(element) < 8:
                            element = "0" + element
                        newByte = newByte + element
                    byte = newByte
                elif len(byte) == 3:
                    byte = str(byte)
                    byte = byte.split("x")
                    byte = byte[1:len(byte)]
                    byte[0] = byte[0][0:2]
                    byte[1] = byte[1][0:2]
                    byte[2] = byte[2][0:2]
                    newByte = ""
                    for element in byte:
                        element =  bin(int(element, 16))
                        element=element[2:len(element)]
                        while len(element)<8:
                            element = "0"+element
                        newByte = newByte+element
                    byte = newByte
            byteMessage = byteMessage+byte
        if len(byteMessage)%8==0:
            if len(byteMessage)%64!=0:
                num = len(byteMessage)/64
                num = int(num)
                num+=1
                num = num*64
                while len(byteMessage)!=num:
                    byteMessage = byteMessage+"00100000"
        return byteMessage

    def toChar(self,message):
        result = ""
        i=0
        num = len(message)/8
        messageList = []
        while i!=num:
            messageList.append(message[i*8:i*8+8])
            i+=1
        index = 0
        while index<len(messageList):
            info = ""
            if int(messageList[index][0:1])==0:
                info = chr(int(messageList[index],2))
                index=index+1
            elif int(messageList[index][0:1])==1 and int(messageList[index][1:2])==1 and int(messageList[index][2:3])==0:
                info = messageList[index]
                info1 = messageList[index+1]
                info = hex(int(info,2))
                info1 = hex(int(info1,2))
                info = info+info1
                try:
                    info = bytes.fromhex(info)
                    info = str(info, 'utf-8')
                except:
                    info = "?"
                index=index+2
            elif int(messageList[index][0:1]) == 1 and int(messageList[index][1:2]) == 1 and int(messageList[index][2:3]) == 1:
                info = messageList[index]
                info1 = messageList[index + 1]
                info2 = messageList[index+2]
                info = hex(int(info,2))
                info1 = hex(int(info1,2))
                info2= hex(int(info2,2))
                info = info[2:4]
                info1= info1[2:4]
                info2 = info2[2:4]
                info = info+info1+info2
                info = bytes.fromhex(info)
                info = str(info,'utf-8')
                index=index+3
            result = result+info
        return result


    def setKey(self,key):
        keyfile = key
        if(len(keyfile))==8:
            ans = []
            byteKey = ""
            keyfile.encode("ascii")
            for element in keyfile:
                tmp= ord(element)
                tmp = bin(tmp)
                tmp = tmp[2:len(tmp)]
                while len(tmp)<8:
                    tmp = "0"+tmp
                ans.append(tmp)
            byteKey = "".join(ans)
            if len(self.key)==0:
                self.key.append(byteKey)
            else:
                self.key[0] = byteKey

    def setFile(self,file):
            temp = file
            if len(self.tempFile)==0:
                self.tempFile.append(temp)
            if len(self.tempFile)!=0:
                self.tempFile[0] = temp


    def process(self,type):
            if type == 0:
                message = self.toBin(self.tempFile[0])
                result = self.processBinMessage(message, self.key[0], 0)
                return result
            else:
                message = self.processBinMessage(self.tempFile[0], self.key[0], 1)
                result = self.toChar(message)
                return result


    def encryption(self,key,file):
        self.setKey(key)
        self.setFile(file)
        result = self.process(0)
        return result    

    def decryption(self,key,file):
        self.setKey(key)
        self.setFile(file)
        result = self.process(1)
        return result

