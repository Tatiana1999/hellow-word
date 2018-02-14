# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import conexion
# Create your models here.

class Enlaces(models.Model):

	url = models.URLField(null=False)
		#fecha_creacion = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __unicode__ (self):
 	    return self.url
