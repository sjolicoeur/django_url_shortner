# -*- coding: utf-8 -*-
from django.db import models
import random, base64, zlib
from django.db.utils import IntegrityError
from django.core.urlresolvers import reverse

################################################################################

def compress(string):
    """ taken and modified from : http://code.activestate.com/recipes/577433-text-compressor-31/ """
    # Get the unique characters and numeric base.
    unique = set(string)
    base = len(unique)
    # Create a key that will encode data properly.
    key = random.sample(unique, base)
    mapping = dict(map(reversed, enumerate(key)))
    while not mapping[string[-1]]:
        key = random.sample(unique, base)
        mapping = dict(map(reversed, enumerate(key)))
    # Create a compressed numeric representation.
    value = 0
    for place, char in enumerate(string):
        value += mapping[char] * base ** place
    # Return the number as a string with the table.
    return str(decode(value))

def decode(value):
    # Change a number into a string.
    array = bytearray()
    while value:
        value, byte = divmod(value, 256)
        array.append(byte)
    return bytes(array)

def generate_shortned_string(url) :
    adler_url = zlib.adler32(url)
    compressed_string = compress ( str(adler_url) )
    shortned_string =  base64.urlsafe_b64encode( compressed_string ).replace("=","").replace("-","").replace("_","")
    return shortned_string


class ShortUrl(models.Model):
    url = models.URLField( verify_exists=True, max_length=255)
    url_bit = models.CharField(  unique=True, default = "-1" , max_length=40)

    def get_absolute_url(self):
        abs_url = reverse('shortner_url', kwargs = {'short_url': self.url_bit})
        return abs_url

    def save(self,*args, **kwargs):
        if self.url_bit == "-1" :
            self.url_bit = generate_shortned_string(self.url)
        try :
            super(ShortUrl,self).save()
        except IntegrityError :
            # regenerate it the random should take care of the collision
            self.url_bit = generate_shortned_string(self.url)
            super(ShortUrl,self).save()