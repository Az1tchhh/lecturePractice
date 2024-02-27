from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class UserrManager(models.QuerySet):
    def get_users(self):
        return self.all()

class Userr(models.Model):
    full_name = models.TextField(max_length=200)
    email = models.TextField(max_length=200, unique=True)
    objects = UserrManager()

class OfficialAnswer(Text):
    user = models.ForeignKey(Userr, on_delete=models.CASCADE, related_name='answer')

class CommentaryType(models.Model):
    name = models.CharField(max_length=200)

class Commentary(Text):
    user = models.ForeignKey(Userr, on_delete=models.CASCADE, related_name='commentary')
    official_answer = models.OneToOneField(OfficialAnswer, on_delete=models.CASCADE)
    commentary_type_id = models.ForeignKey(CommentaryType, on_delete=models.CASCADE)





