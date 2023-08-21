class SavingAccount():
    pass


class CheckingAccount():
    pass

class Bankaaccount(SavingAccount,CheckingAccount):
    pass

class Stock():
    pass

class Bond():
    pass

class RealEstate():
    pass

class Bankaccount(SavingAccount,CheckingAccount):
    pass

class Security(Stock,Bond):
    pass

class InterestBearingltem(Bankaccount,Security):
    pass

class Asset(Bankaccount,RealEstate,Security):
    pass

class Insurableltem(Bankaccount,RealEstate):
    pass

print()
