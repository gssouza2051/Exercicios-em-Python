'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import  urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://play.hbomax.com/page/urn:hbo:page:home')
except urllib.error.URLError:
    print('O site não está acessível')
else:
    print('Consegui entrar no site')