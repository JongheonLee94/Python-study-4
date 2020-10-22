from django.db import models

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    #4.2.5 __str__메서드 추가
    def __str__(self):
        #개개체를 출력할 때 나타날 값
        return "이름 : "+self.site_name +  ", 주소 : " + self.url
