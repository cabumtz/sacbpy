


# excersice
from accounts.models import Bank
from accounts.models import Account
from accounts.models import DebitCard
from accounts.models import BalanceSnapshot

b = Bank(name="BBVA Bancomer")
b.save()

b = Bank(name="HSBC")
b.save()

b = Bank(name="Banorte")
b.save()


Bank.objects.all()

a = Account(bank = b, accountId="13131331331")
a.save()


Account.objects.all()
