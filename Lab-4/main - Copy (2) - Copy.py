from com.agent import Agent
from com.environment import Environment 
from com.environment import Room 

class TwoRoomVaccumCleanerEnvironment(Environment.Environment):
    ''' classdocs ''' 
    def __init__(self, agent,rooms = 2):
        '''Constructor '''

        # #N Numbers of Rooms Program
        # self.rooms = rooms
        # self.rooms = [Room.Room(i, 'dirty') for i in range(1, rooms+1)]
        # self.currentRoom = self.rooms[0]

        # self.r1 = Room.Room('A','dirty') 
        # self.r2 = Room.Room('B','dirty')
        # self.r3 = Room.Room('C','dirty')    #Converting 2 Rooms Program to 3 Rooms Program

        self.agent = agent 
        self.currentRoom = self.rooms[0]    #self.r1 
        self.delay = 1000 
        self.step = 1 
        self.action = ""
        self.score = 0

    def executeStep(self,n=1): 
        for _ in range(0,n):
            self.displayPerception() 
            self.agent.sense(self) 
            res = self.agent.act()
            self.action = res

            #N Numbers of Rooms Program
            if res == "clean":
                self.currentRoom.status = "clean"
                self.score += 25 
            elif res == "right":
                if self.currentRoom == self.rooms[-1]:
                    self.currentRoom = self.rooms[0]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom)+1]
                self.score -= 1
            elif res == "left":
                if self.currentRoom == self.rooms[0]:
                    self.currentRoom = self.rooms[-1]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom)-1]
                self.score -= 1
            
            if self.currentRoom.status == "dirty":
                self.score -= 10

            # if res == 'clean':
            #     self.currentRoom.status = 'clean' 
            # elif res == 'right':    #Converting 2 Rooms Program to 3 Rooms Program
            #     if(self.currentRoom.location == self.r1.location):
            #         self.currentRoom = self.r2
            #     if(self.currentRoom.location == self.r3.location):
            #         self.currentRoom = self.r1
            # elif res == "left":     #Converting 2 Rooms Program to 3 Rooms Program
            #     if(self.currentRoom.location == self.r2.location):
            #         self.currentRoom = self.r3
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
        #Rational Agent
        if all(room.status == "clean" for room in self.environment.rooms):
            return "stop"
        elif self.environment.currentRoom.status == "dirty":
            return "clean"
        else:
            return "right"

        # #N Numbers of Rooms Program
        # if self.environment.currentRoom.status == "dirty":
        #     return "clean"
        # else:
        #     if self.environment.currentRoom == self.environment.rooms[-1]:
        #         return "left"
        #     else:
        #         return "right"

        # if self.environment.currentRoom.status == 'dirty':
        #     return 'clean' 
        # if self.environment.currentRoom.location == 'A': 
        #     return 'right'
        # if self.environment.currentRoom.location == 'B': 
        #     return 'left'
        # if self.environment.currentRoom.location == 'C':    #Converting 2 Rooms Program to 3 Rooms Program
        #     return 'right'
        # return 'left'

class ModelBasedReflexVaccumAgent():
    def __init__(self, model):
        self.model = model
        self.currentRoom = 1
        self.actions = ['clean', 'right', 'left']
        self.step = 1
        self.score = 0

    def updateModel(self, location, status):
        for room in self.model:
            if room['location'] == location:
                room['status'] = status

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]"%(self.step,self.model[self.currentRoom - 1]['status'],self.currentRoom))

    def act(self):
        self.displayPerception()
        ''' return the action to be taken based on the current percept '''
        if self.model[self.currentRoom - 1]['status'] == 'dirty':
            self.score -= 10
            self.updateModel(self.currentRoom, 'clean')
            action = 'clean'
            self.score += 25
        else:
            self.updateModel(self.currentRoom, 'clean')
            if self.currentRoom == len(self.model):
                self.currentRoom = 1
                action = 'left'
                self.score -= 1
            else:
                self.currentRoom += 1
                action = 'right'
                self.score -= 1
        self.step += 1
        return action

if __name__ == '__main__': 
    model = [{'location': 1, 'status': 'dirty'}, {'location': 2, 'status': 'clean'}, {'location': 3, 'status': 'dirty'}]
    vcagent = ModelBasedReflexVaccumAgent(model)
    for i in range(6):
        print(vcagent.act())
    print(f"Total Score: {vcagent.score}")
    # vcagent = VaccumAgent() 
    # env = TwoRoomVaccumCleanerEnvironment(vcagent,6) 
    # env.executeStep(16)
    #print(f"Total Score: {envirnoment.score}")