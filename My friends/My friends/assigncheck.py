from webbrowser import get


def batsman(d):
    name=d.get('name')
    runs=d.get('runs')
    balls=d.get('balls')
    batsman=int(runs/2)
    four=d.get('4')
    six=d.get('6')
    batsman=int(runs/2)
    if batsman>=50:
        batsman+=5
    if batsman>=100: 
        batsman+=10
    
    sr=(runs/balls)*100
    if sr>=80 and sr<100:
        batsman+=2
    if sr>=100:
        batsman+=4
    
    batsman=batsman+four
    batsman=batsman+2*six
    return {'name':name,'batscore':batsman}

def bowler(d):
    name=d.get('name')
    wkt=d.get('wkts')
    balls=d.get('overs')
    runs=d.get('runs')
    bowler=wkt*10
    if wkt>=3:  bowler+5
    if wkt>=5:  bowler+10
    if balls>0:
        er=runs/balls
        if er<=2:   bowler+10
        if er>2 and er<=3.5:    bowler+7
        if er>3.5 and er<=4.5:  bowler+4
    return {'name':name,'bowlscore': bowler}
