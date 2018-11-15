def whale_speak(message):
    if(len(message) ==1):
        return message[0]
    elif(message[0] != message[1]):
        return message[0] + whale_speak(message[1:])
    else:
        return whale_speak(message[1:])

print(whale_speak("hhhooooowwww aaaarrrrreeee yyyyoooouuuu"))