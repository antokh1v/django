from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from .services import count_black_pix


# Create your views here.
def image_upload(request):
    form = ImageForm()
    context = {
        'form': form,
        'error': ''
    }
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = Image.objects.order_by('-id')
            res = count_black_pix(img_obj[0])
            return render(request, 'upload_image/upload_image.html', {'form': form, 'img_obj': img_obj, 'res': res})
        else:
            form = ImageForm()
    return render(request, 'upload_image/upload_image.html', context)
