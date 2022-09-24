from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import Trainer, BlogPost, Feedback, WorkoutProgram, PersonalInfo


def home(request):
    template = 'index.html'
    list_programs = WorkoutProgram.objects.all()[:10]
    list_blog = BlogPost.objects.all()[:10]
    list_trainers = Trainer.objects.order_by('subscribers')[:4]
    list_feedback = Feedback.objects.all()
    context = {
        "list_programs": list_programs,
        "list_blog": list_blog,
        "list_trainers": list_trainers,
        "list_feedback": list_feedback,
    }
    return render(request, template, context)


@csrf_protect
def logingin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('lk')
    else:
        print(user)
        return redirect('start')


@login_required
def lk(request):
    template = 'lk.html'
    return render(request, template)


@login_required
def personalinfo(request):
    template = 'lk-dannye.html'
    context = {
        'info': PersonalInfo.objects.filter(user=request.user)
    }
    print(PersonalInfo.objects.filter(user=request.user)[0].image.url)
    return render(request, template)


def trainers(request):
    template = 'trenery.html'
    pop_trainers = Trainer.objects.order_by('subscribers')[:10]
    list_trainers = Trainer.objects.all()
    context = {
        'pop_trainers': pop_trainers,
        'list_trainers': list_trainers,
    }
    return render(request, template, context)


def trainer(request, trainer_id):
    template = ''
    the_trainer = get_object_or_404(Trainer, pk=trainer_id)
    context = {
        'trainer': the_trainer
    }
    return render(request, template, context)


def programs(request):
    template = 'programmy.html'
    new_programs = WorkoutProgram.objects.order_by('-pub_date')[:10]
    pop_programs = WorkoutProgram.objects.order_by('subscribers')[:10]
    list_programs = WorkoutProgram.objects.all()
    list_feedback = Feedback.objects.all()
    context = {
        "new_programs": new_programs,
        "pop_programs": pop_programs,
        "list_programs": list_programs,
        "list_feedback": list_feedback,
    }
    return render(request, template, context)


def blog(request):
    template = 'blog.html'
    list_blog = BlogPost.objects.order_by('likes')
    context = {
        'list_blog': list_blog
    }
    return render(request, template, context)


def blogpost(request, post_id):
    template = ''
    the_post = get_object_or_404(BlogPost, pk=post_id)
    context = {
        'post': the_post
    }
    return render(request, template, context)


def to_start(request):
    template = 'trenirovatsya.html'
    list_feedback = Feedback.objects.all()
    context = {
        "list_feedback": list_feedback,
    }
    return render(request, template, context)

# def workout(request, id):
#     get_workout = Workout.objects.get(id=id)
#     template = ''
#     context = {
#         'workout': get_workout,
#     }
#     return render(request, template, context)


# def program(request, id):
#     get_program = WorkoutProgram.objects.get(id=id)
#     template = ''
#     context = {
#         'program': ge_program,
#     }
#     return render(request, template, context)
