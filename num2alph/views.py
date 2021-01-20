from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from num2words import num2words
from django.http import JsonResponse
# Create your views here.

@method_decorator(csrf_exempt)

def convert_view(request):
	if request.method == 'POST':
		print(request.headers.get('data'))
		data = request.headers.get('data')
		ans = num2words(data)
		res = {
			'success': True,
			'message': ans
			}
	
	return JsonResponse(res)

