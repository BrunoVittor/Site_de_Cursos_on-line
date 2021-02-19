from django.db import models


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset.filter(models.Q(name_icontains=query) | models.Q(description__icontains=query))


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', blank=True, null=True)
    created_at = models.DateTimeField('Criado em: ', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em: ', auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
