n=int(input('Dati numarul de elemente din vector='))
t=[]
if (n>10)or(n==10):
    print("Introduceti o valoare mai mica ca 10")
    n=int(input('Dati numarul de elemente din vector='))
elif n<10:
    print('Introduceti ',n,' elemente pentru vectorul creat')

for i in range(0,n):
    x=int(input('Introduceti elementele vectorului='))
    t.extend([x])
print(t)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(t[0:5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
b=[]
b=t.copy()
b.reverse()
print(b)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(t)
c.sort(reverse=True)
print(c)
print('d)  afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(t)):
    if t[i]%2==0:
        y=t[i]
        d.extend([y])
print(d)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
e=[]
z=0
for i in range(0,len(t)):
    if t[i]%2==0:
        z=z+1
        y=t[i]
        e.extend([y])
print(sum(e)//z)
print('f)  afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(t)):
    if t[i]%2!=0:
        y=t[i]
        f.extend([y])
print(f)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input("Introduceti x:"))
y=int(input("Introduceti y:"))
g=[]
for i in range(0,len(t)):
    if (t[i]>x)and(t[i]%y!=0):
        y=t[i]
        g.extend([y])
print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
h=[]
for i in range(0,len(t)):
    if (t[i]>x)and(t[i]<y):
        y=t[i]
        h.extend([y])
print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
w=[]
for i in t:
    if i<0:
        w.extend([t.index(i)])
print(w)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
j=[]
for i in range(0,len(t)):
    if ((t[i]>9)and(t[i]<100))or((t[i]>-100)and(t[i]<-9)):
        j.extend([i])
print(j)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=[]
n=list(filter(lambda e: ((e>9)and(e<100))or((e<-9)and(e>-100)), t))
for e in k:
    n.append(t.index(e))
print
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=t.copy()
l[l.index(min(l))]=l[0]
print(l)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m=[]
for i in range(0,len(t)):
    if t[i]%2==0:
        y=t[i]
        m.extend([y])
print(m)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for i in range(0,len(t)):
    if t[i]%3==0:
        y=t[i]
        n.extend([y])
print(n)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori.')
o=[]
for i in t:
    if i>0:
        k=0
        for e in range(1,i+1):
            if (i%e==0):
               k+=1
        if k<=4:
            o.extend([i])
print(o)