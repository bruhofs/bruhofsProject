from cryptographyFramework import *

initializeWrite()
user = "Bruno"
password = "2234"
encryptedText = encryptMessage(user, password, "ahahahahahah")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "ahahahahah 2")
saveNewLine(encryptedText)

