from django.shortcuts import render, redirect
from todolists.models import Item, List
from todolists.forms import ItemForm
from django.core.exceptions import ValidationError

def home_page(request):

	form = ItemForm()
	return render(request, 'home.html',{'form' : form})


def view_list(request, list_id):

	list_ = List.objects.get(id=list_id)
	if request.method == 'POST':
		try:
			item = Item(text=request.POST['text'], list=list_)

			item.full_clean()
			item.save()

			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"
			return render(request, 'list.html', {'list': list_, 'error': error})

	return render(request, 'list.html', {'list': list_})


def new_list(request):

	list_ = List.objects.create()

	try:
		item = Item(text=request.POST['text'], list=list_)

		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {'error': error})

	return redirect(list_)
