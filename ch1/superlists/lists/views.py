from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()

    return render(request, 'list.html', {'items': items})


def new_list(request):
    list_ = List.objects.create()
    # import pdb
    # pdb.set_trace()
    Item.objects.create(text=request.POST['item_text'], user_list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
