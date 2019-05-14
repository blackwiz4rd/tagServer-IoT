from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.models import User
from tag.models import Validate
from django.contrib.auth import authenticate
from datetime import datetime
from django.utils import timezone
# Create your views here.

@csrf_exempt
def new_tag(request):
	if request.method == "POST":
		tag_id = request.POST["tag_id"]
		tag_pass = User.objects.make_random_password(length=16, allowed_chars="ABCDEF0123456789")
		print("tag_id %s tag_pass %s" % (tag_id, tag_pass))

		tag = User.objects.create_user(username=tag_id, password=tag_pass)
		try:
			tag.save()
			return JsonResponse({'status': 'success', 'description': 'saved tag', 'pass': tag_pass})
		except:
			return JsonResponse({'status': 'error', 'description': 'user already exists'})

	return JsonResponse({'status': 'error', 'description': 'not a POST method'})

@csrf_exempt
def new_date(request):
	if request.method == "POST":
		tag_id = request.POST["tag_id"]
		tag_pass = request.POST["tag_pass"]
		user = authenticate(username=tag_id, password=tag_pass)
		if user is not None:
			tag_datetime = request.POST["tag_datetime"]
			date = Validate(tag=user, date=datetime.strptime(tag_datetime, '%m/%d/%y %H:%M:%S'))
			try:
				date.save()
			except:
				return JsonResponse({'status': 'error', 'description': 'tag already registered'})	
			return JsonResponse({'status': 'success', 'description': 'valid until %s' % tag_datetime})
		else:
			return JsonResponse({'status': 'error'})

@csrf_exempt
def get_validity(request):
	if request.method == "POST":
		tag_id = request.POST["tag_id"]
		tag_pass = request.POST["tag_pass"]
		user = authenticate(username=tag_id, password=tag_pass)
		if user is not None:
			validate = Validate.objects.get(tag=user)
			server_date = timezone.localtime(timezone.now())
			print("comparing tag date %s with server date %s" % (validate.date, server_date))
			if server_date < validate.date:
				return JsonResponse({'status': 'success'})
			return JsonResponse({'status': 'error', 'description': 'tag expired since %s' % validate.date})

		return JsonResponse({'status': 'error', 'description': 'wrong user or password'})

@csrf_exempt
def rm_tag(request):
	if request.method == "POST":
		tag_id = request.POST["tag_id"]
		tag_pass = request.POST["tag_pass"]
		user = authenticate(username=tag_id, password=tag_pass)
		if user is not None:
			user.delete()
			return JsonResponse({'status': 'success', 'description': 'removed tag'})

		return JsonResponse({'status': 'error', 'description': 'wrong user or password'})