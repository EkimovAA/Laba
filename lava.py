m = {"m1";2.91, "m2":4.82, "m3":5.88}
tab = {m[1]:(1.808,1.687,1.712,1.675,1.685,1.787,1.682,1.178,1.687,1.829), m[2]:(1.419,1.485,1.381,.1.257,1.347,1.416,1.336,1.318,1.317,1.361), m[3]:(1.289,1.263,1.166,1.268,1.231,1.223,1.187,1.189,1.210,1.284)}
tab_avg= {}

for n in tab:
sum_t = 0
for j in tab[n]:
    sum_t += j
    
tab_avg[n] = round(sum_t/len(tab[n]), 3)

s = 0
s =  ()**(0.5)
sum_t=0 
for n in tab:
    for t in tab[n]
         sum_t = (t - tab_avg[n])**2
s = ((sum_t/len(tab[n]*(len(tab[n]-1)))))**0
x_sl[i] = stats.t.ppf((1+alpha)/2, v-1) * s[n]
