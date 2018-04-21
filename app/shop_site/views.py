from django.shortcuts import render, redirect

def home(request):
	
	if('unicorn_count' not in request.session):
			request.session['unicorn_count'] = 0
	if('eraser_count' not in request.session):
			request.session['eraser_count'] = 0
	if('tp_count' not in request.session):
			request.session['tp_count'] = 0
	if('eggball_count' not in request.session):
			request.session['eggball_count'] = 0
	if('bank_count' not in request.session):
			request.session['bank_count'] = 0
	if('catsushi_count' not in request.session):
			request.session['catsushi_count'] = 0

	return render(request, 'shop_site/index.html')


def process(request):

	if request.method == "POST":

		if("total" not in request.session):
			request.session['total'] = 0


		if('unicorn_count' not in request.session):
			request.session['unicorn_count'] = 0
		if('eraser_count' not in request.session):
			request.session['eraser_count'] = 0
		if('tp_count' not in request.session):
			request.session['tp_count'] = 0
		if('eggball_count' not in request.session):
			request.session['eggball_count'] = 0
		if('bank_count' not in request.session):
			request.session['bank_count'] = 0
		if('catsushi_count' not in request.session):
			request.session['catsushi_count'] = 0

		if 'unicorn' in request.POST:

			request.session['total'] = request.session['total'] + 14.99
			request.session['unicorn_count'] = request.session['unicorn_count'] + 1

		if 'eraser' in request.POST:

			request.session['total'] = request.session['total'] + 6.99
			request.session['eraser_count'] = request.session['eraser_count'] + 1

		if 'tp' in request.POST:

			request.session['total'] = request.session['total'] + 5.50
			request.session['tp_count'] = request.session['tp_count'] + 1

		if 'eggball' in request.POST:

			request.session['total'] = request.session['total'] + 9.99
			request.session['eggball_count'] = request.session['eggball_count'] + 1

		if 'bank' in request.POST:

			request.session['total'] = request.session['total'] + 17.99
			request.session['bank_count'] = request.session['bank_count'] + 1

		if 'catsushi' in request.POST:

			request.session['total'] = request.session['total'] + 9.99
			request.session['catsushi_count'] = request.session['catsushi_count'] + 1
		
		print(request.session['unicorn_count'])

		return redirect('/')

	else:

		return redirect('/')


def checkout(request):

	if request.method == "POST":

		if("total" not in request.session):
			request.session['total'] = 0

		return render(request, 'shop_site/shopping_cart.html')

	else:

		return redirect('/')


def thankyou(request):

	if request.method == "POST":

		if("total" not in request.session):
			request.session['total'] = 0

		return render(request, 'shop_site/thankyou.html')

	else:

		return redirect('/')

def return_home(request):

	if request.method == "POST":
		#clear total
		if("total" in request.session):
			request.session.pop("total")
		#clear items carts
		if('unicorn_count' in request.session):
			request.session.pop("unicorn_count")
		if('eraser_count' in request.session):
			request.session.pop("eraser_count")
		if('tp_count' in request.session):
			request.session.pop("tp_count")
		if('eggball_count' in request.session):
			request.session.pop("eggball_count")
		if('bank_count' in request.session):
			request.session.pop("bank_count")
		if('catsushi_count' in request.session):
			request.session.pop("catsushi_count")

		return render(request, 'shop_site/index.html')

	else:

		return redirect('/')


