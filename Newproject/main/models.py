from django.db import models


class New_preject(models.Model):
    file_name = models.TextField('file_name')
    file_size = models.IntegerField('file_size')
    format_file = models.CharField('format_file', max_length=50)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'