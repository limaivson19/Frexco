from django.db import models
from django import forms


class Cadastro(models.Model):
    login = models.CharField(max_length=255)
    senha = models.CharField(blank=True, max_length=255)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.login

class FormCadastro(forms.ModelForm):
    class Meta:
        model = Cadastro
        exclude = ()
