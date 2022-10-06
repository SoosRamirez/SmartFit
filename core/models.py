from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Trend(models.Model):
    name = models.CharField(max_length=20, verbose_name='Раздел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'


class Direction(models.Model):
    name = models.CharField(max_length=20, verbose_name='Раздел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'


class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    picture_src = models.ImageField()
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    read_time = models.CharField(max_length=5, default='')
    author = models.TextField()
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, default=1, null=True)

    def like(self):
        self.likes = self.likes + 1
        self.save()

    def view(self):
        self.views = self.views + 1
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField()


class Trainer(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    trend = models.ForeignKey(Trend, on_delete=models.SET_NULL, null=True)
    picture_src = models.ImageField()
    direction = models.ManyToManyField(Direction, through='Workout')

    workouts = models.IntegerField(default=0)
    programs = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)

    def new_workout(self):
        self.workouts = len(Workout.objects.filter(trainer_id=self.id))
        self.save()

    def lose_workout(self):
        self.workouts = self.workouts - 1
        self.save()

    def new_program(self):
        self.programs = len(WorkoutProgram.objects.filter(trainer_id=self.id))
        self.save()

    def lose_program(self):
        self.programs = self.programs - 1
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'


class WorkoutProgram(models.Model):
    name = models.CharField(max_length=30)
    picture_src = models.ImageField()
    length = models.TimeField(auto_created=True, default='00:00:00')
    calories = models.IntegerField(default=0)
    amount_of_workouts = models.IntegerField(default=0)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default='0')
    directions = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=200)
    # subscribers = models.ManyToManyField(User, through='Subscription', default=0)
    pub_date = models.DateTimeField(auto_created=True, default='2001-01-01T00:00:00.000000+03:00')
    CHOICES = [
        ('1', 'Новичек'),
        ('2', 'Любитель'),
        ('3', 'Продвинутый'),
        ('4', 'Профессионал'),
    ]
    level = models.CharField(max_length=1, choices=CHOICES)

    def save(self, *args, **kwargs):
        self.trainer.new_program()
        super().save(*args, **kwargs)
        self.trainer.new_program()

    def delete(self, using=None, keep_parents=False):
        self.trainer.lose_program()
        super().delete(using=None, keep_parents=False)

    def add_workout(self):
        self.workouts = len(Workout.objects.filter(trainer_id=self.trainer.id))
        self.save()

    def lose_workout(self):
        self.workouts = self.workouts - 1
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа'


class Workout(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    video = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default='')
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, default=1, null=True)
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        self.trainer.new_workout()
        self.program.add_workout()
        super().save(*args, **kwargs)
        self.trainer.new_workout()
        self.program.add_workout()

    def delete(self, using=None, keep_parents=False):
        self.program.lose_workout()
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренировка'


# class Subscription(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
#     workout_stopped = models.IntegerField(default=0)
#
#     def save(
#             self, force_insert=False, force_update=False, using=None, update_fields=None
#     ):
#         super().save(self)
#         self.program.trainer.subscribers = self.program.trainer.subscribers + 1
#         self.program.trainer.save()
#
#     def delete(self, using=None, keep_parents=False):
#         self.program.trainer.subscribers = self.program.trainer.subscribers - 1
#         self.program.trainer.save()


# ready
class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    instagram = models.CharField(max_length=20)
    mass = models.IntegerField()
    height = models.IntegerField()
    sex = models.CharField(max_length=20)
    birthdate = models.DateField()


# ready
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mass = models.IntegerField()
    hips = models.IntegerField()
    arms = models.IntegerField()
    chest = models.IntegerField()
    legs = models.IntegerField()
    waist = models.IntegerField()
    prev_pic_front = models.ImageField(default='', null=True)
    cur_pic_front = models.ImageField(default='')
    prev_pic_back = models.ImageField(default='', null=True)
    cur_pic_back = models.ImageField(default='')
    prev_pic_side = models.ImageField(default='', null=True)
    cur_pic_side = models.ImageField(default='')

    def save(self, *args, **kwargs):
        if len(Progress.objects.filter(user=self.user.id)) > 0:
            self.prev_pic_side = Progress.objects.filter(user=self.user.id).order_by('-date')[0].cur_pic_side
            self.prev_pic_front = Progress.objects.filter(user=self.user.id).order_by('-date')[0].cur_pic_front
            self.prev_pic_back = Progress.objects.filter(user=self.user.id).order_by('-date')[0].cur_pic_back
        if len(Progress.objects.filter(user=self.user.id)) > 5:
            Progress.objects.filter(user=self.user.id).order_by('date')[0].delete()
        super().save(self)


# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     num = models.IntegerField()
#     type = models.CharField(max_length=20)
#     status = models.BooleanField()
#     date_subscribed = models.DateField(auto_created=True)
#     promo = models.CharField(max_length=20, null=True)
#     sum = models.IntegerField()
#     date_expired = models.DateField(null=True)
