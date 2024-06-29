class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return' %.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)
    def __add__(self,other):
        sum=Time()
        #self->time2
        #self->time3
        sum.hour=self.hour+other.hour
        sum.minute=self.minute+other.minute
        sum.second=self.second+other.second
        if sum.second>=60:
            sum.second-=60
            sum.minute+=1
        if sum.minute>=60:
            sum.minute-=60
            sum.minute+=1
        return sum
time1=Time(10,25,55)
print(time1)
time2=Time(10,55)
print(time2)
time3=time1+time2
print(time3)
    

