from cProfile import run
from multiprocessing.sharedctypes import Value


'''def batsman():
    pointp1=0
    pointp2=0
    p1={'name':'Virat Kohli','role':'bat','runs':112,'4':10,'6':0,'balls':119,'field':0}
    p2={'name':'du Plessis','role':'bat','runs':120,'4':11,'6':2,'balls':112,'field':0}    
    if p1['runs']>2:
        pointp1= p1["runs"]//2
    if p2['runs']>2:
        pointp2=p2['runs']//2    
    if p1['runs']>50:
        pointp1=pointp1+5
    if p2['runs']>50:
        pointp2=pointp2+5   
    if p1['runs']>100:
        pointp1=pointp1+10
    if p2['runs']>100:
        pointp2=pointp2+10
    strike_rate1=p1['runs']/p1['balls']*100
    if strike_rate1>100:
        pointp1=pointp1+4
    if strike_rate1>80: 
        pointp1=pointp1+2
    strike_rate2=p2['runs']/p2['balls']*100 
    if strike_rate2>100:
        pointp2=pointp2+4
    elif strike_rate2>80: 
        pointp2=pointp2+2
    pointp1=pointp1+((p1['4']*1)+p1['6']*2)
    pointp2=pointp2+((p2['4']*1)+p2['6']*2)
    #print(pointp1,pointp2)    
    print({'name':p1['name'],'batscore':pointp1}) 
    print({'name':p2['name'],'batscore':pointp2})   
batsman()'''

def bowler():
    point1=0
    point2=0
    point3=0
    p3={'name':'Bhuvneshwar Kumar','role':'bowl','wkts':1,'overs':10,'runs':71,'field':1}
    p4={'name':'Yuzvendra Chahal','role':'bowl','wkts':2,'overs':10,'runs':45,'field':0}
    p5={'name':'Kuldeep Yadav','role':'bowl','wkts':3,'overs':10,'runs':34,'field':0}
    point1=p3['wkts']*10  
    if p3['wkts']==5:
        point1=point1+10
    elif p3['wkts']==3:
        point1=point1+5
    else:
        point1=point1+0
    point2=p4['wkts']*10
    if p4['wkts']==5:
        point2=point2+10
    elif p4['wkts']==3:
        point2=point2+5
    else:
        point2=point2+0
    point3=p5['wkts']*10
    if p5['wkts']==5:
        point3=point3+10
    elif p5['wkts']==3:
        point3=point3+5
    else:
        point3=point3+0
    economy_rate1=p3['runs']/p3['overs']
    if economy_rate1<2:
        point1=point1+10
    elif economy_rate1>2:
        point1=point1+7
    elif economy_rate1<3.5:
        point1=point1+7
    elif economy_rate1 in range(3.5,4.5):
        point1=point1+4
    economy_rate2=p4['runs']/p4['overs']
    if economy_rate2<2:
        point2=point2+10
    elif economy_rate2>2:
        point2=point2+7
    elif economy_rate2<3.5:
        point2=point2+7
    elif economy_rate2 in range(3.5,4.5):
        point2=point2+4
        
    print(point1,point2)

    
    #economy_rate3=p5['runs']/p5['overs']
    return
bowler()

