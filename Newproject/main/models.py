from django.db import models


class New_project(models.Model):
    file_name = models.TextField('file_name')
    file_size = models.IntegerField('file_size')
    format_file = models.CharField('format_file', max_length=25)
    changed_format = models.CharField('changed_format', max_length=25)
    some_info = models.TextField('some_info')

    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'