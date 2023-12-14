n = int(input())

ps = []
vps = []

for _ in range(n):
    ps.append(input())

for element in ps:
    open = 0
    close = 0
    answer = 0
    for parenthesis in element :
        if parenthesis == '(':
            open += 1
        else :
            close += 1
            if open < close :
                answer = 'NO'
                break
    if open == close and answer != 'NO':
        answer = 'YES'
    else : 
        answer = 'NO'
    vps.append(answer)
    
for element in vps:
    print(element)