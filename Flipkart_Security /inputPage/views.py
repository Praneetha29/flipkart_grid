from django.shortcuts import render
from django.http import JsonResponse
from .models import data_file
from .forms import UploadFileForm
import inputPage.quick_search as qs
import inputPage.full_search as fs
import inputPage.ingest as ingester


# Create your views here.
# def save_text(request):
#     global saved_text
#     if request.method == "POST":
#         data = request.POST
#         saved_text = data.get("text", "")
#         print(saved_text)
#         return JsonResponse({"message": "Text saved successfully."})


def form_view(request):
    print(16)
    if request.method == 'POST':
        print(3)
        fileList = request.FILES.getlist("upload_form")
        for file in fileList:
            fileSave = data_file.objects.create(file1=file)
            # print(form)
            fileSave.save()

            print("file saved: " + fileSave.file1.path)

        # print(str(form))
        # if form.is_valid():
        #     form.save()
        #     print(1)
        # qs.get_result("""NO ONE SHOULD HAVE role: roles/owner
        #      NO ONE SHOULD HAVE role: roles/editor
        #      NO ONE SHOULD HAVE role: roles/owner""")
    # context = {'form':data_file()}
    print(str(request.POST))
    ruleStr = request.POST.get('rules')
    print(ruleStr)
    # ingester.runs()
    result_dict = fs.main(ruleStr)
    output_text = result_dict.get('output_text', '').strip()
    print('-'*34)
    print(output_text)
    context = {
        'output': output_text
    }
    return render(request, 'inputPage/input.html', context)


def button_full(request):
    fs.get_result()


#
def button_quick(request):
    pass


def input_view(request):
    return render(request, 'inputPage/input.html')
