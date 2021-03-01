# This Naomi plugin implements a simple elapse timer.

import time
from naomi import plugin

class SimpleTimerPlugin(plugin.SpeechHandlerPlugin):
    
    def intents(self):
        return {
            'TimerIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'NumberKeyword': [
                                'ONE',
                                'TWO',
                                'THREE',
                                'FOUR',
                                'FIVE'
                            ]
                        },
                        'templates': [
                            "SET TIMER {NumberKeyword} SECONDS",
                            "SET {NumberKeyword} SECOND TIMER"
                        ]
                    }
                },
                'action': self.handle
            }
        }

    def handle(self, intent, mic):
        """
        Once the brain detected the keywords above,
        it trigger this part
        """
        NUMBERS = {
            'ONE' :    1,
            'TWO' :    2,
            'THREE' :  3,
            'FOUR' :   4,
            'FIVE' :   5
        #}
        ERROR = ''
        NUMBER ='ONE'

        # Check for actual number inputs
        try:
            NUMBER = intent['matches']['NumberKeyword'][0]
            # print (" Number is: " + NUMBER)      # For debug
        except KeyError:
            ERROR = "Could not understand input. Please try again!"
        try:
            ETimer = NUMBERS[NUMBER]
        except KeyError:  
            ERROR = "Timer input out of range!"
        # Handle error conditions
        if ERROR != '':
            mic.say(self.gettext("ERROR: %s!" % ERROR))
        # Run elapse timer   
        else:
            mic.say(self.gettext("Start " + NUMBER  + " second timer!"))
            time.sleep(ETimer)
            mic.say(self.gettext(NUMBER + " second timer finished!"))
