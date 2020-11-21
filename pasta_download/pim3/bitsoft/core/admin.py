from django.contrib import admin
from .models import Uf
from .models import Cidade
from .models import Cliente
from .models import TipoCriptoativo
from .models import Investimento
from .models import SmartContract
from .models import TipoOperacao
from .models import Operacao
from .models import Cargo
from .models import Funcionario


admin.site.register(Uf)
admin.site.register(Cidade)
admin.site.register(Cliente)
admin.site.register(TipoCriptoativo)
admin.site.register(Investimento)
admin.site.register(SmartContract)
admin.site.register(TipoOperacao)
admin.site.register(Operacao)
admin.site.register(Cargo)
admin.site.register(Funcionario)
