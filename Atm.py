class atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        
    def CashWithdrawl(self):
        print('CashWithDrawled')  
         
    def BalanceEnquiry (self):
        print('Enquiry')
        
    def Deposit (self):
        print('Deposited')
        
    def OtherServices (self):
        print('OtherServices')        
        
SBI=atm(22,2929)    
print(SBI.CashWithdrawl())    
