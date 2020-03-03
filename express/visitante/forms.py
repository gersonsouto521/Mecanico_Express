from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=50,
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": ""
                }
            )
        )
    email     = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "exemplo@email.com"
                }
            )
        )

    telefone     = forms.CharField(max_length=11,
        widget=forms.TextInput(
            
            attrs={
                    "class": "form-control", 
                    "placeholder": "71 9xxxx-xxxx",
                }
            )
        )

    placa     = forms.CharField(max_length=7,
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "XXX-0000"
                }
            )
        )  
    

    MARCAS =( 
    ("1", "Fiat"), 
    ("2", "Ford"), 
    ("3", "Chevrolet"), 
    ("4", "Wolksvagem"), 
    ("5", "Hyundai"), 
    ("6", "Outras"), 
    ) 
    marca = forms.ChoiceField(choices = MARCAS) 

    SERVICOS = (
    ("1", "Lavagem Veicular"), 
    ("2", "Manutenção Preventiva"), 
    ("3", "Revisão Leve"), 
    ("4", "Lavagem de Motor"), 
    ("5", "Reparo Gerais"), 
    ("6", "Revisão Pesada"), 
    )
    servico = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                    choices=SERVICOS)


    observacoes   = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem",
                    "rows":5, "maxlength":500,                 
                }
            )
)