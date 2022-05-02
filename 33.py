import json

with open ("333.json","r") as f:
    d=json.loads(f.read())
    f.close()
    name = input("Enter your name:")
    print("Welcome",name,"to the quiz")
    score=0
    for i in d:
       print(i)
       ans = input("Enter the answer :")
       if ans==d[i]:
           
            
        print("Correct answer")
        score=score+1
        print("your score now is",score)
       else:
           print("Wrong answer")
           print("your score now is",score)
result=name,'your final score is :',score
print(result)
with open ("result.json","w") as f:
    d=json.dumps(d)
    f.close()
