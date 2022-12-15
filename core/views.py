from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

from SmartFit.settings import BASE_DIR
from SmartFit import settings
from .models import Trainer, BlogPost, Feedback, WorkoutProgram, PersonalInfo, Question, Direction, \
    Trend, Subscription, Workout, Payment, Progress


# Done
def home(request):
    template = 'SFindex.html'
    list_programs = WorkoutProgram.objects.all()[:10]
    list_blog = BlogPost.objects.all()[:10]
    list_trainers = Trainer.objects.order_by('subscribers')
    list_feedback = Feedback.objects.all()
    list_questions = Question.objects.all()
    context = {
        "list_programs": list_programs,
        "list_blog": list_blog,
        "list_trainers": list_trainers,
        "list_feedback": list_feedback,
        "list_questions": list_questions,
	"dir": BASE_DIR,
    }
    print(request.user_agent.is_mobile)
    return render(request, template, context)


# ready
@csrf_protect
def logingin(request):
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('lk')
    else:
        print(user)
        return redirect('start')


# ready
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


# ready
@login_required
def lk(request):
    template = 'SFpersonal.html'
    return render(request, template)


# ready
@csrf_protect
@login_required
def personalinfo(request):
    info = PersonalInfo.objects.filter(user=request.user)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES['image']
            filename = image._get_name()
            fd = open(settings.MEDIA_URL + str(filename), 'wb')
            for chunk in image.chunks():
                fd.write(chunk)
            fd.close()
            if info:
                PersonalInfo.objects.filter(user=request.user).update(image=request.FILES['image'])
            else:
                PersonalInfo.objects.create(user=request.user, image=request.FILES['image'])
        name = request.POST["name"]
        surname = request.POST["surname"]
        mobile = request.POST["mobile"]
        instagram = request.POST["instagram"]
        mass = int(request.POST["mass"])
        height = int(request.POST["height"])
        email = request.POST["email"]
        sex = request.POST["sex"]
        birthdate = request.POST["birth"]
        level = request.POST["level"]
        if info:
            PersonalInfo.objects.filter(user=request.user).update(name=name, surname=surname, mobile=mobile,
                                                                  instagram=instagram, mass=mass, height=height,
                                                                  email=email, sex=sex, birthdate=birthdate,
                                                                  level=level)
        else:
            PersonalInfo.objects.create(user=request.user, name=name, surname=surname, mobile=mobile,
                                        instagram=instagram,
                                        mass=mass, height=height, email=email, sex=sex, birthdate=birthdate,
                                        level=level)
    template = 'SFpersonalinfo.html'
    info = PersonalInfo.objects.filter(user=request.user)
    if info:
        context = {
            'info': get_object_or_404(PersonalInfo, user=request.user)
        }
    else:
        return render(request, template)
    return render(request, template, context)


# ready
@login_required
def personalprogramms(request):
    template = 'SFpersonalprograms.html'
    e = WorkoutProgram.objects.filter(subscribers=request.user)
    for i in e:
        i.workouts = Workout.objects.filter(program=i)
    context = {
        'list_programs': e,
    }
    print(context)
    return render(request, template, context)


# no template
@login_required
def personalworkouts(request):
    template = 'SFpersonalworkouts.html'
    context = {
    }
    return render(request, template, context)


# ready
@csrf_protect
@login_required
def personalprogress(request):
    template = 'SFpersonalprogres.html'
    progress = Progress.objects.filter(user=request.user)
    print(progress)
    if request.method == "POST":
        if request.FILES:
            cur_front = request.FILES.get('cur_front', False)
            cur_side = request.FILES.get('cur_side', False)
            cur_back = request.FILES.get('cur_back', False)
            prev_front = request.FILES.get('prev_front', False)
            prev_side = request.FILES.get('prev_side', False)
            prev_back = request.FILES.get('prev_back', False)
            if cur_front:
                filename = cur_front._get_name()
                fd = open(settings.MEDIA_URL + str(filename), 'wb')
                for chunk in cur_front.chunks():
                    fd.write(chunk)
                fd.close()
                if progress:
                    Progress.objects.filter(user=request.user).update(cur_pic_front=cur_front,
                                                                      last_update=timezone.now())
                else:
                    Progress.objects.create(user=request.user, cur_pic_front=cur_front)
            if prev_front:
                filename = prev_front._get_name()
                fd = open(settings.MEDIA_URL + str(filename), 'wb')
                for chunk in prev_front.chunks():
                    fd.write(chunk)
                fd.close()
                if progress:
                    Progress.objects.filter(user=request.user).update(prev_pic_front=prev_front)
                else:
                    Progress.objects.create(user=request.user, prev_pic_front=prev_front)
            if cur_side:
                filename = cur_side._get_name()
                fd = open(settings.MEDIA_URL + str(filename), 'wb')
                for chunk in cur_side.chunks():
                    fd.write(chunk)
                fd.close()
                if progress:
                    Progress.objects.filter(user=request.user).update(cur_pic_side=cur_side, last_update=timezone.now())
                else:
                    Progress.objects.create(user=request.user, cur_pic_side=cur_side)
            if prev_side:
                filename = prev_side._get_name()
                fd = open(settings.MEDIA_URL + str(filename), 'wb')
                for chunk in prev_side.chunks():
                    fd.write(chunk)
                fd.close()
                if progress:
                    Progress.objects.filter(user=request.user).update(prev_pic_side=prev_side)
                else:
                    Progress.objects.create(user=request.user, prev_pic_side=prev_side)
            if cur_back:
                filename = cur_back._get_name()
                fd = open(settings.MEDIA_URL + str(filename), 'wb')
                for chunk in cur_back.chunks():
                    fd.write(chunk)
                fd.close()
                if progress:
                    Progress.objects.filter(user=request.user).update(cur_pic_back=cur_back, last_update=timezone.now())
                else:
                    Progress.objects.create(user=request.user, cur_pic_back=cur_back)
            if prev_back:
                filename = prev_back._get_name()
                fd = open(settings.MEDIA_URL + str(filename), 'wb')
                for chunk in prev_back.chunks():
                    fd.write(chunk)
                fd.close()
                if progress:
                    Progress.objects.filter(user=request.user).update(prev_pic_back=prev_back)
                else:
                    Progress.objects.create(user=request.user, prev_pic_back=prev_back)
        if progress:
            mass = request.POST.get('mass', False)
            waist = request.POST.get('waist', False)
            hips = request.POST.get('hips', False)
            chest = request.POST.get('chest', False)
            arms = request.POST.get('arms', False)
            legs = request.POST.get('legs', False)
            if mass:
                progress.update(mass=int(mass))
            if waist:
                progress.update(waist=int(waist))
            if hips:
                progress.update(hips=int(hips))
            if chest:
                progress.update(chest=int(chest))
            if arms:
                progress.update(arms=int(arms))
            if legs:
                progress.update(legs=int(legs))
        else:
            if request.POST['mass']:
                Progress.objects.create(user=request.user, mass=int(request.POST['mass']))
            if request.POST['waist']:
                Progress.objects.create(user=request.user, waist=int(request.POST['waist']))
            if request.POST['hips']:
                Progress.objects.create(user=request.user, hips=int(request.POST['hips']))
            if request.POST['chest']:
                Progress.objects.create(user=request.user, chest=int(request.POST['chest']))
            if request.POST['arms']:
                Progress.objects.create(user=request.user, arms=int(request.POST['arms']))
            if request.POST['legs']:
                Progress.objects.create(user=request.user, legs=int(request.POST['legs']))
    context = {
        'progress': Progress.objects.filter(user=request.user)
    }
    return render(request, template, context)


# ready
@login_required
def subscription(request):
    template = 'SFpersonalsubscription.html'
    context = {
        'payments': Payment.objects.filter(user=request.user)
    }
    return render(request, template, context)


# ready
def trainers(request):
    template = 'SFtrainers.html'
    pop_trainers = Trainer.objects.order_by('subscribers')[:10]
    list_trainers = Trainer.objects.all()
    directions = Direction.objects.all()
    context = {
        'pop_trainers': pop_trainers,
        'list_trainers': list_trainers,
        'directions': directions,
    }
    return render(request, template, context)


# ready
def trainer(request, trainer_id):
    template = 'SFtrainer.html'
    the_trainer = get_object_or_404(Trainer, pk=trainer_id)
    list_programs = WorkoutProgram.objects.filter(trainer_id=trainer_id)
    list_trainers = Trainer.objects.all()
    list_questions = Question.objects.all()
    list_feedback = Feedback.objects.all()
    context = {
        'trainer': the_trainer,
        'list_programs': list_programs,
        'list_trainers': list_trainers,
        'list_questions': list_questions,
        'list_feedback': list_feedback,
    }
    return render(request, template, context)


# ready
def subscribe(request, program_id):
    if request.user.is_authenticated:
        print(program_id)
        s = Subscription.objects.filter(user=request.user, program_id=program_id)
        if len(s) == 0:
            Subscription.objects.create(user=request.user, program_id=program_id)
    return redirect('program', program_id)


# to do
def programs(request):
    template = 'SFprograms.html'
    new_programs = WorkoutProgram.objects.order_by('-pub_date')[:10]
    pop_programs = WorkoutProgram.objects.order_by('subscribers')[:10]
    list_programs = WorkoutProgram.objects.all()
    list_feedback = Feedback.objects.all()
    list_questions = Question.objects.all()
    context = {
        "new_programs": new_programs,
        "pop_programs": pop_programs,
        "list_programs": list_programs,
        "list_feedback": list_feedback,
        'list_questions': list_questions,
        'directions': Direction.objects.all(),
        'trend': Trend.objects.all()
    }
    return render(request, template, context)


# ready
def program(request, program_id):
    get_program = WorkoutProgram.objects.get(id=program_id)
    template = 'SFprogram.html'
    context = {
        'program': get_program,
        'trainers': WorkoutProgram.objects.filter(trainer_id=get_program.trainer_id),
    }
    print(get_program.subscribers)
    return render(request, template, context)


# no template
# def workout(request, id):
#     get_workout = Workout.objects.get(id=id)
#     template = ''
#     context = {
#         'workout': get_workout,
#     }
#     return render(request, template, context)

# ready
def blog(request):
    template = 'SFblogpage.html'
    context = {
        'list_blog': BlogPost.objects.order_by('likes')
    }
    return render(request, template, context)


# no template
def blogpost(request, post_id):
    template = 'SFblogpost'
    context = {
        'post': get_object_or_404(BlogPost, pk=post_id)
    }
    return render(request, template, context)


# ready
@csrf_protect
def purchase(request):
    username = request.POST.get('login', False)
    password = request.POST.get('password', False)
    passwordrep = request.POST.get('passwordrep', False)
    if username and passwordrep and password:
        u = User.objects.all()
        for i in u:
            if username == i.username:
                return redirect('home')
        if passwordrep == password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            newuser = authenticate(request, username=username, password=password)
            if newuser is not None:
                login(request, newuser)
                return redirect('lk')
    else:
        return redirect('home')
