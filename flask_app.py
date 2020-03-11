from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

FILE_SSKJ="sbsj-new.txt"
FILE_50K="50k-dict.txt"
K=4

@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    st=request.args.get("st_besed", K)
    sumniki=request.args.get("sumniki", False)
    slovar=request.args.get("slovar", "sskj")
    try: 
        val = int(st)
    except ValueError:
        val = K
    if slovar=="50k":
        words = random_sampler(FILE_50K,val)
    else:
        words = random_sampler(FILE_SSKJ,val)
    if sumniki:
        #print(sumniki)
        for i,w in enumerate(words):
            words[i]=words[i].replace("č","c")
            words[i]=words[i].replace("š","s")
            words[i]=words[i].replace("ž","z")
            #print(words)
    #return f'{escape(" ".join(words))}<br>{escape("".join(words))}'
    return render_template('generator.html', 
        geslo_pres=" ".join(words), 
        geslo_brezpres="".join(words), 
        st_besed=val, 
        sumniki=sumniki,
        slovar=slovar)

def random_sampler(filename,k):
    sample = []
    with open(filename, 'rb') as f:
        f.seek(0,2)
        filesize = f.tell()
        
        random_set = sorted(random.sample(range(filesize), k))
        
        for i in range(k):
            f.seek(random_set[i])
            f.readline()
            sample.append(f.readline().rstrip().lower().decode('utf-8'))
            
        return sample