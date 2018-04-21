class User:
    def __init__ (self, id, name, department):
        self.level = 1
        self.currentXp = 0
        self.nextLevel = 50
        self.attendanceStreak = 0
        self.id = id
        self.name = name
        self.department = department
        self.achievements = instantiateAchievements

    def instantiateAchievements():
        array = []
        array + Milestone("Weakly Streak", 10).generateMilestones(10, 5)
        return array

    def giveXp (x):
        self.currentXp += x
        if self.currentXp >= self.nextLevel:
            level += 1
            self.nextlevel = self.nextLevel * (1+log2(level))


    def getValues (param):
        return self.currentXp

    def endStreak (x):
        self.attendanceStreak = 0
    
    def incrementStreak():
        self.attendanceStreak += 1

class Achievement():
    def __init__(self, name, xp):
        self.xp = xp
        self.name = name
        self.goal = 50
        self.achieved = false

    def compareValues(user):
        return user.getValues(name).equal(goal)

    def giveAchievement(user):
        user.achievements.push(name)
        user.giveXp(xp)
        self.achieved = true

class Milestone(Achievement):
    def __init__():
        super(self, name, xp)

    def generateMilestones(amount, factor):
        array = []
        i = 0
        while i < amount:
            array.push(Achievement(self.name + " " + i, i * factor))
            i += 1
        return array
