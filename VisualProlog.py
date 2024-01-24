from random import choice
from experta import *

class Light(Fact):
    pass #can pass anything to display

class RobotCrossStreet(KnowledgeEngine):#knowledgeEngine is class provided by experta proces rules
    @Rule(Light(color='green')) # @ is a decorator associated with Knowllegde engine defines condition
    def green_light(self):
        print("walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

    @Rule(AS.light << Light(color=(L('yellow') | L('blinking-yellow')))) #AS is a keyword in experta it binds to the keyword if conditiion matches , << use to match following condition
    def cautious(self, light):
        print("Be cautious because light is", light["color"])

engine = RobotCrossStreet()
engine.reset()
engine.declare(Light(color=choice(['green', 'yellow', 'blinking-yellow', 'red'])))
engine.run()
