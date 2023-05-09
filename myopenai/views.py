from django.shortcuts import render
from django.conf import settings
    
import openai

openai.api_key = settings.OPENAI_API_KEY

