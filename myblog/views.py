from django.shortcuts import render
from django.utils import timezone
from .models import Post,TestModel,UserModel
from myblog.forms import PostForm,TestForm,UserEntryForm
from django.http import HttpResponseRedirect

# Create your views here.
def post_list(request):

    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    userform = UserEntryForm()
    return render(request,'myblog/post_list.html',{'userform':userform})
    #return render(request,'myblog/post_list.html',{'text':'timezone.now'})

def test_model(request):
    return render(request,'myblog/test_model.html')

def post_form_test(request):
    if request.method == 'GET':
        form = PostForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = PostForm()
    return render(request, 'myblog/post_list.html', {'form': form})

def post_fetch_data(request):
    #postform = PostForm(data=request.POST)
    posts = Post.objects.filter(author=request.POST.get('name'))
    return render(request,'myblog/detailsviewform.html',{'posts':posts})

def details_view(request):
    #posts = Post.objects.all()
    #return render(request,'myblog/detailsviewform.html',{'posts':posts})
    posts = Post.objects.filter(author=request.POST.get('name'))
    return render(request,'myblog/detailsviewform.html',{'posts':posts})

def test_form(request):
    form=TestForm()
    return render(request,'myblog/test_model.html',{'form':form})

def fetch_test(request):
    fetchdata = TestModel.objects.filter(username=request.POST.get('name'))
    return render(request,'myblog/fetch_data.html',{'fetchdataname':fetchdata})

def user_entry(request):
    form = UserEntryForm()
    return render(request,'myblog/userentry.html',{'form':form})

def user_save_data(request):
	#adding values to the models
    print("Beforeee:",request)
    usermodel = UserModel()
    usersaveform = UserEntryForm(data=request.POST)
    print(request.POST)
    name = request.POST['name']
    if usersaveform.is_valid():
        data = usersaveform.cleaned_data
        print(data)
        usermodel.username = data['name']
        print(usermodel.username)
        usermodel.save()
    print (usersaveform.errors)
    #return HttpResponseRedirect('/')#redirects to home
    return render(request,'myblog/userentry.html',{'form':usersaveform})

def user_fetch_alldata(request):
    #usermodel = UserModel.objects.filter(username=request.POST.get('name'))
    print("Beforeee:",request)
    usermodel = UserModel.objects.all()
    return render(request,'myblog/userfetchdata.html',{'usermodel':usermodel})

def user_data_form(request):
    userForm = UserEntryForm(data=request.POST)
    name = request.POST['name']
    print(name)
    if userForm.is_valid():
        data = userForm.cleaned_data
        print(data)
        usermodel= UserModel.objects.filter(username=data['name'])
        print(usermodel)
    return render(request,'myblog/userfetchdata.html',{'usermodel':usermodel})
