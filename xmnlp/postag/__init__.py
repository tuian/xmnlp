# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# -------------------------------------------#
# author: sean lee                           #
# email: xmlee97@gmail.com                   #
#--------------------------------------------#

"""MIT License
Copyright (c) 2018 Sean
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sys
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')
    
from ..config import path as C_PATH
from . import postag

postagger = None
def loader():
    global postagger
    if postagger == None:
        try:
            postagger = postag.Postag()
            model_path = C_PATH.postag['model']['dag']
            hmm_seg_path = C_PATH.postag['model']['seg']
            hmm_tag_path = C_PATH.postag['model']['tag']
            postagger.load(model_path, hmm_seg_path, hmm_tag_path)
        except:
            pass
    
userdict = None
def set_userdict(fpath):
    loader()
    global userdict
    if userdict == None:
        postagger.userdict(fpath)
    
def seg(doc, hmm=True):
    loader()

    postagger.set_hmm(hmm)
    words = list(postagger.seg(doc))
    return words

def tag(doc, hmm=True):
    loader()

    postagger.set_hmm(hmm)
    if sys.version_info[0] == 2:
        doc = doc.decode('utf-8')

    word_tags = postagger.tag(doc)
    return word_tags

def load(dag, seg_hmm=None, tag_hmm=None):
    global postagger
    postagger = postag.Postag()
    postagger.load(dag, seg_hmm, tag_hmm)
