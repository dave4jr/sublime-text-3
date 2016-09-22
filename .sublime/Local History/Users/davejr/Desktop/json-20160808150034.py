if request.is_ajax() and request.method == "POST":
	form = MemberForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponse(json.dumps(data), 'application/json')
		
else: