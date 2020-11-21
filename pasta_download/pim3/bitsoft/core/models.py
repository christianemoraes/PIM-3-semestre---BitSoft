from django.db import models


class Uf (models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Cidade (models.Model):
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE, related_name='uf_id')
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='cidade_id')
    cpf_cliente = models.CharField(max_length=11)
    cpf_respon = models.CharField(max_length=11)
    nome = models.CharField(max_length=80)
    data_nasc = models.CharField(max_length=10)
    endereco = models.CharField(max_length=50)
    num_celular = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=15)
    num_conta = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class TipoCriptoativo (models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Tipos de Criptoativos"


class Investimento (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='investimento_clientes')
    tipo_criptoativo = models.ForeignKey(TipoCriptoativo, on_delete=models.CASCADE, related_name='criptoativos')
    data = models.CharField(max_length=10)
    hora = models.CharField(max_length=6)
    descricao = models.CharField(max_length=80)

    def __str__(self):
        return self.data

class SmartContract (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contrato_clientes')
    data_inicial = models.CharField(max_length=10)
    data_final = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Smart Contracts"


class TipoOperacao (models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Tipos de Operações"


class Operacao (models.Model):
    investimento = models.ForeignKey(Investimento, on_delete=models.CASCADE, related_name='investimentos')
    tipo_operacao = models.ForeignKey(TipoOperacao, on_delete=models.CASCADE, related_name='tipo_operacao')
    data = models.CharField(max_length=10)
    hora = models.CharField(max_length=6)
    descricao = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Operações"


class Cargo (models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Funcionario (models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='cargo')
    matricula = models.CharField(max_length=15)
    cpf_funcio = models.CharField(max_length=11)
    nome_funcio = models.CharField(max_length=80)
    rg = models.CharField(max_length=10)
    endereco = models.CharField(max_length=80)
    filiacao = models.CharField(max_length=80)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.cpf_funcio
