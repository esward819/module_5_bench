from django.shortcuts import render
from app.forms import SumForm
# Create your views here.
def root(request): 
    form = SumForm(request.GET)
    if form.is_valid():
        x = form.cleaned_data['x']
        y = form.cleaned_data['y']
        z = form.cleaned_data['z']
        result = (x*y*z)
        return render(request, "root.html", {"form": form, "result": result})
    else:
        form = SumForm()
        return render(request, "root.html", {"form": form})