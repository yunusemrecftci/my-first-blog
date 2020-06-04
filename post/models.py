from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar',on_delete=models.CASCADE,related_name="post")
    title = models.CharField(max_length=120,verbose_name='başlık')
    text = RichTextUploadingField(verbose_name='yazı')
    date =models.DateTimeField(verbose_name='tarih',auto_now = True)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True,editable=False,max_length=130)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug':self.slug})
    def get_create_url(self):
        return reverse('post:create')
    
    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_detele_url(self):
        return reverse('post:detele', kwargs={'slug': self.slug})   
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug 
    def save(self, *args, **kwargs):
            self.slug = self.get_unique_slug()
            return super(Post, self).save(*args, **kwargs)
       
    class Meta:
        ordering = ['-date']