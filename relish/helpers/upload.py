# -*- coding: utf-8 -*-
import os
import random
import string

def upload_to(path):
    def upload_callback(instance, filename):
        random_fname = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for x in range(16))
        random_fname += os.path.splitext(filename)[-1]
        return '%s/%s' % (path.rstrip('/'), random_fname)
    return upload_callback