from django.shortcuts import render
from Dashboard.forms import ImageForm
from Dashboard.models import Image

def profile(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form =ImageForm()
    img = Image.objects.all()
    diction={
        "form":form,
        "img":img
        }
    return render(request,'index.html', context=diction)
