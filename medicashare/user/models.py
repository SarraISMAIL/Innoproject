from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import post_save
from PIL  import Image
post_category=(
    ('R','Request'),
    ('D','Donation'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug_title = models.CharField(max_length=100,null=True)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    current_place =models.CharField(max_length=50)
    show_post =models.CharField(max_length=6)
    post_type = models.CharField(choices=post_category,null=True,max_length=100)

    def __str__(self):
        return 'Title: {} {} , created by {}'.format(self.post_type,self.title,self.author)
    
    

    class Meta:
        ordering = ('post_date', )


class Notification(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='receiver',on_delete=models.CASCADE) 
    sender = models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE ,null=True) 
    notification_date =models.DateTimeField(default=timezone.now)
    status =models.CharField(max_length=6)   
    def __str__(self):
        return f' from {self.sender} to {self.post.author} about {self.post.title}'
    class Meta:
        ordering =('-notification_date',)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_images')
    phone_number = models.CharField(max_length=12)

    #email_verif = random code created while registeration
    #others ...


    def __str__(self):
        return f'{self.user} profile '
        #resize photo 
    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""

def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
    

post_save.connect(create_profile,sender=User)
