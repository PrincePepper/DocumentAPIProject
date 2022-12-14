import json
from collections import deque
from datetime import datetime


class DocumentClass:

    def __init__(self, number: int = None, date=None, comment: str = None):
        self.number = number
        self.date = self.defDate(date)
        self.comment = comment
        self.json: json = None
        self.__list_product = deque()

    def initDateStroke(self, nameproduct: str,
                       amountproduct: int,
                       priceproduct: float,
                       sumproduct: float):
        name = nameproduct
        amount = amountproduct
        price = priceproduct
        sum = sumproduct
        self.__list_product.appendleft([name, amount, price, sum])

    def defDate(self, datestroke) -> datetime:
        if datestroke is None:
            return datetime.strptime("01.01.0001", '%d.%m.%Y')
        datetime_object = datetime.strptime(datestroke, '%d.%m.%Y')
        return datetime_object

    def getDocument(self) -> json:
        content = self.__list_product.copy()
        captions_content = ['name', 'amount', 'price', 'sum']
        captions_document = ['number', 'date', 'comment']
        prepared_content = [dict(zip(captions_content, row)) for row in content]

        prepared_document = [dict(zip(captions_document, row)) for row in
                             [[self.number, str(self.date.date()), self.comment], ]]
        prepared_document.append(prepared_content)
        # self.json = json.dumps(prepared_document, ensure_ascii=False)
        # aaa=json.loads(self.json)
        return prepared_document

    def serializeDocument(self, path: str):
        with open(path, 'r', encoding="utf-8") as f:
            strokes = f.readlines()
            self.number, self.date, self.comment = strokes[0].replace('\n', '').split(',')
            self.date = self.defDate(self.date)
            strokes.pop(0)
            strokes.pop(0)
            strokes.pop(0)
            for i in strokes:
                self.__list_product.append(i.replace('\n', '').split(','))

    def serializeDocumentString(self, string: str):
        strokes = string.replace('\n', '').split(',')
        self.number, self.date, self.comment = int(strokes[0]), strokes[1], strokes[2]
        self.date = self.defDate(self.date)
        for i in range(8):
            strokes.pop(0)
        for i in range(0, len(strokes), 4):
            self.__list_product.append(
                [strokes[i], strokes[i + 1], strokes[i + 2], strokes[i + 3]])

    def deserializeDocument(self, path: str):
        with open(path, 'w') as outfile:
            if self.json is None:
                return "I dont have document"
            jsonStr = json.loads(self.json)
            json.dump(jsonStr, outfile)

# doc = DocumentClass()
# doc.serializeDocumentString(
#     "12,18.09.2022,?????? ??????????????????????,,???????????????????????? ????????????,????????????????????,????????,??????????,????????????,2,12.5,25,??????????????????,1,3,3,????????????????,10,5,50")
# # docs = doc.getDocument()[0]
# print(111)
# doc.serializeDocument("test_document.txt")
# doc.getDocument()
# doc.deserializeDocument("test_document2.txt")
# print(docs)
