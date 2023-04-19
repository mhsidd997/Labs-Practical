import random

class Environment(object):
    def __init__(self, numb=3): #numb is number of rooms and should be greater than equal to 2 (n>=2)
        self.LocationCondition = {}
        for i in range(numb):
            self.LocationCondition['Area ' + str(i+1)] = random.randint(0,1)

class ReflexAgent(Environment):
    def __init__(self, Environment):
        Score = 0
        vaccumLoc = random.randint(0,1)
        if vaccumLoc == 0:
            print("Vaccum is at Area " + str(vaccumLoc))
            if Environment.LocationCondition['Area '+str(vaccumLoc)] == 0:
                print("Area " + str(vaccumLoc) + " is Cleaned")
                print("Moving to Area " + str(vaccumLoc + 1))
                Score -= 1
            if (Environment.LocationCondition['Area '+str(vaccumLoc+1)])+1 == 1:
                print("Area " + str(vaccumLoc + 1) + " is Dirty...")
                print("Area " + str(vaccumLoc + 1) + " is Cleaned")
                Score -= 10
                Environment.LocationCondition['Area '+str(vaccumLoc+1)] == 0
                Score += 25
        elif vaccumLoc == 1:
            print("Vaccum is at Area " + str(vaccumLoc))
            if Environment.LocationCondition['Area '+str(vaccumLoc)] == 0:
                print("Area " + str(vaccumLoc) + " is Cleaned")
                print("Moving to Area " + str(vaccumLoc+1))
                Score -= 1
            if (Environment.LocationCondition['Area '+str(vaccumLoc+1)])+1 == 1:
                print("Area " + str(vaccumLoc + 1) + " is Dirty...")
                print("Area " + str(vaccumLoc + 1) + " is Cleaned")
                Score -= 10
                Environment.LocationCondition['Area '+str(vaccumLoc + 1)] == 0
                Score += 1

        print("Performance Measurement: " + str(Score))
    
theEnv = Environment()
theVacuum = ReflexAgent(theEnv)