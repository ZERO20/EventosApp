#encoding:utf-8
from django.db import models
import os
import itertools
from django.template.defaultfilters import slugify
from django.template import defaultfilters
from django.contrib.auth.models import User


class CatConceptoEstatus(models.Model):
    descripcion = models.CharField(max_length=50)

class CatEstatus(models.Model):
    descripcion = models.CharField(max_length=50)
    concepto_estatus = models.ForeignKey(CatConceptoEstatus)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name = 'estatus'
        verbose_name_plural = 'Catalogo de Estatus'
        unique_together = ['descripcion']


class CatCategoriasEspacios(models.Model):
    def get_upload_path(instance, filename):
        carpetaImagenes =  slugify(instance.categoria)
        ruta = os.path.join("media/categotegorias/", carpetaImagenes)
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (slugify(instance.categoria), ext)
        return os.path.join(ruta, filename)

    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    icono = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    usuario = models.ForeignKey(User)
    fecha_registro = models.DateField(auto_now_add=True)
    cat_estatus = models.ForeignKey(CatEstatus)

    def save(self, *args, **kwargs):
        self.slug = orig = defaultfilters.slugify(self.categoria)
        for x in itertools.count(1):
            if not CatCategoriasEspacios.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)
        super(CatCategoriasEspacios, self).save(*args, **kwargs)

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ['descripcion']
        verbose_name = 'Categoria '
        verbose_name_plural = 'Catalogo de Categorías'