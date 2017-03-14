#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16)
    password = forms.CharField(widget=forms.PasswordInput())


class PhotoForm(forms.Form):
    photo = forms.FileField(label=u'头像')


class SearchByForm(forms.Form):
    CHOICES = [
        (u'ISBN', u'ISBN'),
        (u'书名', u'书名'),
        (u'作者', u'作者')
    ]

    search_by = forms.ChoiceField(
        label='',
        choices=CHOICES,
        widget=forms.RadioSelect(),
        initial=u'书名',
    )


class SearchForm(forms.Form):
    keyword = forms.CharField(
        label='',
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': u'请输入需要检索的图书信息',
            'name': 'keyword',
        })
    )
