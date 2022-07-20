from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from scripts import util

def home(request):
    return render(request, 'main.html')

def predict(request):
    # name = request.POST['name']
    # print(name)
    return HttpResponse('Ok')

@csrf_exempt
def test(request):
    if request.method == 'POST':
        image_name = str(request.POST.get('image'))
        image_path = image_name.replace("fakepath", "Users\Omar Elbachyr\PycharmProjects\Django_Football_Image_Classifier\scripts\\test_images")
        print('prediction')
        print(image_path)
        util.load_saved_artifacts()
        print(util.classify_image(None, image_path))
    return HttpResponse('om')

