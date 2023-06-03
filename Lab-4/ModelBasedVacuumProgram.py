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