import re
def valUse(use):
    if not use[0].isupper():
        print('A primeira letra precisa ser maiúscula')
        return False

    elif re.search('[^a-zA-Z0-9\s]', use):
        print('O usuário não pode conter caractéres especiais')
        return False

    elif ' ' in use:
        print('O usuário não pode conter espaços')
        return False

    elif len(use) > 30:
        print('O usuário não pode conter mais que 30 caractéres')
        return False

    else:
        return True
def valSen(sen):
    if len(sen) > 10:
        print('A senha deve ter menos de 10 caractéres')
        return False

    elif not re.search('[^a-zA-Z0-9\s]', sen):
        print('A senha deve conter um caracter especial')
        return False
    
    elif not re.search('\d', sen):
        print('A senha deve conter um número')
        return False

    elif not re.search('[A-Z]',sen):
        print('A senha deve conter uma letra maiúscula')
        return False

    elif not re.search('[a-z]',sen):
        print('A senha deve conter uma letra minúscula')
        return False
    
    else: 
        return True

def valMsg(msg):
    if len(msg) > 70:
        print('A mensagem deve conter menos de 70 caractéres')
        return False
    
    else: 
        return True

    
    

