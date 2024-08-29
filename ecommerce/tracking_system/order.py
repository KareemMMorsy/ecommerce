class order():
    import csv
    import os
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent
    
    
    
    def __init__(self,orderId,orderName,userName,status):
        self.orderId=orderId
        self.orderName=orderName
        self.userName=userName
        self.status=status
    
    @classmethod
    def getAllOrders(cls):
        filepath=cls.os.path.join(cls.BASE_DIR,'orders.csv')
        print(filepath)
        with open(filepath, newline='') as csvfile:
            reader = cls.csv.reader(csvfile, delimiter=' ', quotechar='|')
            rowlist=[]
            for i,row in enumerate(reader):
                orderId,orderName,userName,status=row[0].split(',')
                rowlist.append({'orderId':orderId,'orderName':orderName,'userName':userName,'status':status})
            return rowlist
    
    def saveInCsv(self):
        with open('./orders.csv', 'a', newline='') as csvfile:
            writer = self.csv.writer(csvfile,delimiter=',')
            writer.writerow([self.orderId,self.orderName,self.userName,self.status])
        
        
