from django.shortcuts import render, redirect

# Create your views here.
# def home(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST or None)
#
#         if form.is_valid():
#             form.save()
#             all_items = TaskDb.objects.all()
#             messages.success(request, ('New item added..'))
#             return render(request, 'index.html', {'all_items': all_items})
#
#     else:
#         all_items = TaskDb.objects.all()
#         return render(request, 'index.html', {'all_items': all_items})

def home(request):
    return render(request, 'index.html')
