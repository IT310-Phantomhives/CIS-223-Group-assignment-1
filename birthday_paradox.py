import random
people=5;
birth_day=list(range(1,365));
while(people<=50):
    birth_Day=[];
    count=0;
    loop=1000;
    while(loop!=0):
        count=0;
        for i in range(people):
            day=random.randint(0,365);
            birth_Day.append(day);
        for i in range(people):
            bday=birth_Day[i];
        for j in range(i+1,people):
            if(bday==birth_Day[j]):
                count=count+1;
            break;
        loop=loop-1;
    print("For people",people,"\nProbability:",count,"/",1000);
people=people+1;