

import  json


dictData = {
    "bookName":"yushu",
    "bookType":"ISBN"
}

def writeJson():
    with open('data.txt', 'w', encoding='utf-8') as  file:
        file.write(json.dumps(dictData,indent=2))
        file.close()

def readJson():
    with open('data.txt', 'r', encoding='utf-8') as file:
        jsonData = file.read()
        jsonDic = json.loads(jsonData)
        print(jsonDic['bookName'])

def operateJson():
    pass
