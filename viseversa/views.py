﻿from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	test_get_text = request.GET['usertext']
	words = test_get_text.split()
	number_of_words = len(words)
	reversed_text = test_get_text[::-1]
	return render(request, 'reverse.html', {'test_get_text':test_get_text, 'reversedtext': reversed_text, 'number_of_words': number_of_words})
