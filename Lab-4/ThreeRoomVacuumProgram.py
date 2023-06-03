from com.agent import Agent
from com.environment import Environment 
from com.environment import Room 

class ThreeRoomVaccumCleanerEnvironment(Environment.Environment):
    ''' classdocs ''' 
    def __init__(self, agent,rooms = 2):
        '''Constructor '''

        self.r1 = Room.Room('A','dirty') 
        self.r2 = Room.Room('B','dirty')
        self.r3 = Room.Room('C','dirty')

        self.agent = agent 
        self.currentRoom = self.r1 
        self.delay = 1000 
        self.step = 1 
        self.action = ""

    def executeStep(self,n=1): 
        for _ in range(0,n):
            self.displayPerception() 
            self.agent.sense(self) 
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.currentRoom.status = 'clean' 
            elif res == 'right':
                if(self.currentRoom.location == self.r1.location):
                    self.currentRoom = self.r2
                if(self.currentRoom.location == self.r3.location):
                    self.currentRoom = self.r1
            elif res == "left":
                if(self.currentRoom.location == self.r2.location):
                    self.currentRoom = self.r3

            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]"%(self.step,self.currentRoom.status,self.currentRoom.location))

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" %(self.step,self.action))

    def delay(self,n=100):
        self.delay = n

class VaccumAgent(Agent.Agent):
    ''' classdocs'''
    def __init__(self): 
        '''Constructor ''' 
        pass

    def sense(self,env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean' 
        if self.environment.currentRoom.location == 'A': 
            return 'right'
        if self.environment.currentRoom.location == 'B': 
            return 'left'
        if self.environment.currentRoom.location == 'C':
            return 'right'
        return 'left'

def checkInput(x):
    if x <= 10:
        x = int(input("Enter number greater than 10: "))
        return checkInput(x)
    else:
        return x

if __name__ == '__main__':
    x = int(input("Enter Steps of Executions, it should be greater than 10: "))
    s = checkInput(x) 
    vcagent = VaccumAgent() 
    env = ThreeRoomVaccumCleanerEnvironment(vcagent) 
    env.executeStep(s)