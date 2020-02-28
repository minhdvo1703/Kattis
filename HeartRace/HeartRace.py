#input number of cases
n = int(input())
for i in range(n):
    #input beats and time (in second)
    b,p = input().split()
    b = int(b)
    p = float(p)

    #calculate BPM and ABPM
    bpm = (60*b)/p
    abpm = 60/p

    #print the result (min abpm, bpm, max abpm)
    print(format(bpm-abpm,'.4f'), format(bpm,'.4f'), format(bpm+abpm,'.4f'));


