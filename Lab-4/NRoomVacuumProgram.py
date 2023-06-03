from com.agent import Agent
from com.environment import Environment 
from com.environment import Room 

class NRoomVaccumCleanerEnvironment(Environment.Environment):
    ''' classdocs ''' 
    def __init__(self, agent,rooms = 2):
        '''Constructor '''

        self.rooms = rooms
        self.rooms = [Room.Room(i, 'dirty') for i in range(1, rooms+1)]
        self.currentRoom = self.rooms[0]

        self.agent = agent 
        self.currentRoom = self.rooms[0] 
        self.delay = 1000 
        self.step = 1 
        self.action = ""

    def executeStep(self,n=1): 
        for _ in range(0,n):
            self.displayPerception() 
            self.agent.sense(self) 
            res = self.agent.act()
            self.action = res

            if res == "clean":
                self.currentRoom.status = "clean"
            elif res == "right":
                if self.currentRoom == self.rooms[-1]:
                    self.currentRoom = self.rooms[0]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom)+1]
            elif res == "left":
                if self.currentRoom == self.rooms[0]:
                    self.currentRoom = self.rooms[-1]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom)-1]
                
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
        if self.environment.currentRoom.status == "dirty":
            return "clean"
        else:
            if self.environment.currentRoom == self.environment.rooms[-1]:
                return "left"
            else:
                return "right"

def checkInput(x,c):
    if(c == 'r'):
        if x <= 2:
            x = int(input("Enter number of Rooms greater than 2: "))
            return checkInput(x,'r')
        else:
            return x
    else:
        if x <= 10:
            x = int(input("Enter number greater than 10: "))
            return checkInput(x,'c')
        else:
            return x

if __name__ == '__main__':
    x = int(input("Enter number of Rooms, it should be greater than 2: "))
    r = checkInput(x,'r')
    x = int(input("Enter steps of execution, it should be greater than 10: "))
    s = checkInput(x,'s')  
    vcagent = VaccumAgent() 
    env = NRoomVaccumCleanerEnvironment(vcagent,r) 
    env.executeStep(s)