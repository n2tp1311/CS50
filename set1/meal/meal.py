def main():
    strTime, apM = input('What time is it? ').lower().split(' ')
    time = convert(strTime)
    am  = ['a.m.', 'a.m', 'am']
    pm  = ['p.m.', 'p.m', 'pm']
    print(time, apM)
    if apM:
        if apM in am:
            if 7 <= time <= 8:
                print('breakfast time') 
        elif apM in pm:
            if 0 <= time <= 1 and 12 <= time < 13:
                print('lunch time')
            elif 6 <= time <= 7:
                print('dinner time')
        else:
            print('time to play')
    else:
        if 7 <= time <= 8:
            print('breakfast time')
        elif 12 <= time <= 13:
            print('lunch time')
        elif 18 <= time <= 19:
            print('dinner time')
        else:
            print('time to play')

def convert(time): 
    h, m = time.split(':')   
    h = float(h)    
    m = float(m) / 60
    if 0 <= m < 1:
        return h + m
    else:
        return ValueError('Minute (0-59)')

if __name__ == '__main__':
    main()