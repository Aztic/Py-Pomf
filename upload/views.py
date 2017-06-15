from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Upload
import random
import datetime
import string #for generating a random name
import hashlib #for hash in response
import os

def random_name(ini,fin):
	options = string.ascii_uppercase + string.ascii_lowercase
	q = random.randrange(ini,fin)
	r = ''
	while q > 0:
		r += random.choice(options)
		q-=1
	return r

def le_name(ini,fin,ext):
	generate = random_name(ini,fin)
	while os.path.exists(os.path.join(os.getcwd(),'files',generate+ext)):
		generate = random_name(ini,fin)
	return generate

@csrf_exempt
def index(request):
	if request.method != 'POST':
		return HttpResponse()
	data ={
		"success": False
	}
	if 'files[]' in request.FILES:
		sha1 = hashlib.sha1()
		extension = '.' + request.FILES['files[]'].name.split('.')[-1]
		name = le_name(5,64,extension)
		path = os.path.join(os.getcwd(),'files',name+extension)
		try:
			with open(path,'wb+') as f:
				for chunk in request.FILES['files[]'].file:
					sha1.update(chunk)
					f.write(chunk)
			size = os.path.getsize(path)
			element = Upload(user_id=0,filename=name+extension,hash_value=sha1.hexdigest(),original_filename=request.FILES['files[]'].name,size=size,created=datetime.datetime.now())
			element.save()
			data['success'] = True
			data['files'] = [{'hash':sha1.hexdigest(),'name':name+extension,'url':'soon tm','size':size}]
		except:
			print('im an error :D')
			pass
	return JsonResponse(data)




# Create your views here.
