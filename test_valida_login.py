from valida_login import *

def test_valUse():
    assert valUse('a') == False
    assert valUse('A#') == False
    assert valUse('A a') == False
    assert valUse('Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == False
    assert valUse('A') == True

def test_valSen():
    assert valSen('+2Aaaaaaaaaaaaaaaaaaaaaaaaaaaa') == False
    assert valSen('Aa+') == False
    assert valSen('aA2') == False
    assert valSen('a2=') == False
    assert valSen('A2=') == False
    assert valSen('Aa=9') == True

def test_valMsg():
    assert valMsg('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == False
    assert valMsg('aaaassssssaaaassssssaaaassssssaaaassssssssaaaassssss')