#print("Entrando no laço...")
#for i in range(10):
#    print(i)
#    if (i==5):
#        break
#print("Saindo do laço...")

print("Entrando no laço...")
i = 0
while(i<10):
    i+=1
    if (i%2==0):
        continue
    print(i)
    print("Saindo do laço...")