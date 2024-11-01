from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import registrationForm, userUpdateForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, eventForm, EventCatorogyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Ppicture, eventModel, BookedUser, EventCatorogy
from django.db.models import Q

# Create your views here.
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        event_data = (eventModel.objects.filter(event_name__icontains=q)|eventModel.objects.filter(event_location__icontains=q)|eventModel.objects.filter(event_descriptions__icontains=q)|eventModel.objects.filter(event_date__icontains=q))
    else:
        event_data = eventModel.objects.all().values()
    return render(request, 'eventapp/index.html', {'event_data': event_data})

#card detail views
def detailview(request, id):
    event_details = eventModel.objects.filter(id=id).values()
    return render(request, 'eventapp/detailview.html', {'event_details':event_details})

# For Registration / Signup
def signup(request):
    UserRegF = registrationForm() 
    if request.method == 'POST':        
        UserRegF = registrationForm(request.POST)
        if UserRegF.is_valid():
            UserRegF.save()
            return redirect('home')
    return render(request, 'eventapp/signup.html', {'userCre': UserRegF })

# For Login
def signin(request):
    form  = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('profile')
            else:
                return redirect('home')
    return render(request, 'eventapp/login.html', {"loginForm": form})
#------------------------------------------------------------------------------------------
@login_required
def profile(request):
    user_id = request.session.get('user_id')
    find_user = User.objects.filter(id=user_id).values()
    picture = Ppicture.objects.filter(user_id=user_id).values()
    events = eventModel.objects.all().values()
    
    booked_info = BookedUser.objects.filter(user_id=user_id).values()
    list_booed_userinf = []
    for x in booked_info:
        user_id_booked = x['user_id']
        event_data_id = x['event_data_id']
        booked_infox = eventModel.objects.filter(id=event_data_id).values()
        list_booed_userinf.append(booked_infox)   
    

    context = {
        'picture': picture,
        'user': find_user,
        'booked_infox':list_booed_userinf,
        'events':events,
        
    }
    return render(request, 'eventapp/profile.html', context)




@login_required
def logMeOut(request):
    logout(request)
    return redirect('home')    

@login_required
def edit(request, id):
    user_from_db = User.objects.filter(id=id).values()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_from_db.update(first_name=first_name, last_name=last_name, email=email)
        return redirect('profile')
    return render(request, 'eventapp/update.html', {'user_info':user_from_db})

@login_required
def createEvent(request):
    event_form = eventForm()
    user_id = request.session.get('user_id')
    login_user = User.objects.filter(id=user_id).values()
    login_username = ''
    for username in login_user:
        login_username = username['username']

    if request.method == 'POST':
        event_form = eventForm(request.POST)
        if event_form.is_valid():  
            form_user = str(event_form.cleaned_data['user'])            
            if form_user == login_username:

                event_form.save()
            else:
                return redirect('createevent')
            return redirect('profile')
    
    return render(request, 'eventapp/createevent.html', {'event_form':event_form})



@login_required
def eventDel(request, id):
    user_id_seeion = request.session.get('user_id')
    event_date = eventModel.objects.filter(id=id).values('user_id')
    user_id_for = 0
    for user_id_for in event_date:
        user_id_for = user_id_for['user_id']
        
    if user_id_for == user_id_seeion:
        delete_event = get_object_or_404(eventModel, id=id)
        delete_event.delete()
        return  redirect('profile')
    else:
        return redirect('profile')


@login_required
def updateEvent(request, id):
    form_1 = eventForm()
    user_id_seeion = request.session.get('user_id')
    event_date = eventModel.objects.filter(id=id).values('user_id')
    user_id_for = 0
    for user_id_for in event_date:
        user_id_for = user_id_for['user_id']
        
    if user_id_for == user_id_seeion:   

        update_data = get_object_or_404(eventModel, id=id)
        if request.method == 'POST':
            form_1 = eventForm(request.POST, instance=update_data)
            if form_1.is_valid():
                form_1.save()
                return redirect('profile')
        else:
            form_1 = eventForm(instance=update_data)
    else:
        return redirect('profile')
    return render(request, 'eventapp/eventupdate.html', {'form_1': form_1})   


@login_required
def bookUserFind(request, id):
    user_id_seeion = request.session.get('user_id')
    print(request.method)
    if request.method == 'GET':
        book_status = True        
        for_user = BookedUser.objects.filter(user_id__exact = user_id_seeion, event_data_id__exact=id).values()
        if len(for_user) == 0:
            db_data = BookedUser(book_status=book_status, user_id=user_id_seeion, event_data_id=id, )
            db_data.save()
        return redirect('profile')

@login_required
def EventCatorogyview(request):
    ecatform = EventCatorogyForm()
    print(request.method)
    if request.method == 'POST':        
        ecatform = EventCatorogyForm(request.POST)
        if ecatform.is_valid():
            ecatform.save()
        return redirect('profile')
    return render(request, 'eventapp/eventcat.html', {'eventcat': ecatform})