from accounts.models import Bank
from accounts.models import Account
from accounts.models import DebitCard
from accounts.models import BalanceSnapshot

from django.contrib import admin

admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(DebitCard)
admin.site.register(BalanceSnapshot)
