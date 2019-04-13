from pynput import keyboard
from pynput.keyboard import Key, Controller
moves =[False, False]

class KeyLogger():
    def __init__(self):
        self.moose = "9"
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()
        self.moves = [False, False]
        self.action = 0
    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            self.moose = key
            print(key)
            if key.char == '1':
                self.moves[1] = True
            if key.char == '0':
                self.moves[0] = True
        
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        return 

    def on_release(self, key):
        print('{0} released'.format(
            key))
        #self.moose = ''
        moose = key
        if key.char == "0":
            self.moves[0] = False
        if key.char == "1":
            self.moves[1] = False
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    def actions(self):
        if self.moves[1] == True:
            self.action = 1

        else:
            self.action = 0
        return self.action




class KeyboardController():
    def __init__(self):
        self.moose = "yeah"
        self.keyboard = Controller()
    
    def press(self, key):
        self.keyboard.press(Key.key)

    def release(self, key):
        self.keyboard.release(Key.key)

    def press_release(self, key):
        self.keyboard.press(Key.key)
        self.keyboard.release(Key.key)
    
    def typeing(self, string):
        self.keyboard.type(string)



# Collect events until released
#with keyboard.Listener(
        #on_press=on_press,
        #on_release=on_release) as listener:
    #listener.join()

# ...or, in a non-blocking fashion:
#listener = keyboard.Listener(
    #on_press=on_press,
    #on_release=on_release)
#listener.start()
#listener = keyboard.Listener(on_press=on_press,on_release=on_release)
#listener.start()
test = KeyLogger()
test
while True:
    #with keyboard.Listener(
        #on_press=on_pressjjj) as listener:
        #on_release=on_release) as listener:
        #key = listener.join()
    #print(test.moose)
    #print(test.moves)
    if test.moves[0] == True and test.moves[1] == True:
        print('Willie is sexy')
    #print("moose")
    #print(moose)
    #input('lalala')
    
    
    
    
