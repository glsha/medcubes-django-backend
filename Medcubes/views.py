from django.shortcuts import render
from .forms import MedcubesForm

# Create your views here.

def form_detail(request):
    if request.method == 'POST':
        form = MedcubesForm(request.POST)
        if form.is_valid():
            form.save()

    # unbound form(no data associated with it)
    form = MedcubesForm()
    return render(request, 'form.html', {'form': form})