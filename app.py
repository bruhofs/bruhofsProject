from cryptographyFramework import *
from valida_login import *

brk = False

while not brk:
    use = input('Digite seu usuário --> ')
    brk = valUse(use)

brk = False

while not brk:
    sen = input('Digite sua senha --> ')
    brk = valSen(sen)

brk = False

while not brk:
    msg = input('Digite a mensagem --> ')
    brk = valMsg(msg)

encryptedText = encryptMessage(use,sen,msg)
saveNewLine(encryptedText)