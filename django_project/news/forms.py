from django.forms import DateTimeInput, ModelForm, Textarea, TextInput

from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новости'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата и время публикации'
            })
        }
