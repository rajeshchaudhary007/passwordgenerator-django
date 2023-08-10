import string
import re
import random

from django.shortcuts import render
from django.views import View
from .forms import PasswordGenForm


class Index(View):
    def get(self,request):
        form = PasswordGenForm()
        context ={
            'form': form
        }
        return render(request, 'passwordgen/index.html',context)
    
    def post(self,request):
        form = PasswordGenForm(request.POST)
        
        if form.is_valid():
            available_characters = string.ascii_letters + string.digits
            
            if form.cleaned_data['include_symbols']:
                available_characters += string.punctuation
                
            if form.cleaned_data['remove_similar_characters']:
                ambigiuous_characters = ['Z', '2', 'l', '1', '0', 'O', 'o']
                available_characters = re.sub('|'.join(ambigiuous_characters), '', available_characters)
            
            password = ''.join(random.choice(available_characters) for i in range(form.cleaned_data['length']))
            
            context = {
                'form': form,
                'password': password,
            }
        return render(request, 'passwordgen/index.html', context )
            