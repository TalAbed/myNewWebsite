from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, FieldList, IntegerField, FormField, StringField

app = Flask(__name__)
app.config["SECRET_KEY"] = "RandomString"

class number(FlaskForm):
    n = IntegerField("how many items are we going to divide?")

    s = SubmitField("Submit")

class A (FlaskForm):
    itemA = IntegerField("player A item")

class B (FlaskForm):
    itemB = IntegerField("player B item")

class ItemsA (FlaskForm):
    n=4
    def __init__(self, n):
        self.n = n
        super(ItemsA, self).__init__(n)
    itemsA = FieldList(FormField(A), min_entries=n)
    s = SubmitField("Submit")

class ItemsB (FlaskForm):
    num=0
    def __init__(self, n):
        self.num = n
    itemsB = FieldList(FormField(B), min_entries=num)
    s = SubmitField("Submit")

# class Items (FlaskForm):
#     num=4
#     def __init__(self, num=0):
#        self.num = num
#        super(Items, self).__init__(num)
#     playerA = FieldList(FormField(A), min_entries=num)
#     playerB = FieldList(FormField(B), min_entries=num)
#     s = SubmitField("Submit")

class Items (FlaskForm):
    playerA = StringField("Enter player A list of items")
    playerB = StringField("Enter player B list of items")
    s = SubmitField("Submit")

# @app.route('/')
# def numOfItems():
#     form = number()
#     return render_template("enterNum.html", form=form)

#@app.route('/check')
#def checking():
 #   num = request.form('n')
 #   print(num)
#  return render_template("checkNum.html", num)

@app.route('/')
def enterItems():
    form = Items()
    return render_template("enterItems.html", form=form)
    

def remove(playerA: list, playerB: list):
    playerA.remove(playerB[0])
    playerB.remove(playerA[0])
    del playerA[0]
    del playerB[0]
    return playerA, playerB

def BT (playerA, playerB):
    A = []
    B = []
    CP = []
    while len(playerA)>0:
        if playerA[0] != playerB[0]:
            A.append(playerA[0])
            B.append(playerB[0])
            remove(playerA, playerB)
        else:
            CP.append(playerA[0])
            del playerA[0]
            del playerB[0]
    return A, B, CP

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

@app.route('/answer', methods=["POST"])
def answer():
    #l = request.form
    listA=list(eval(request.form["playerA"]))
    listB=list(eval(request.form["playerB"]))
    #al = {x:l[x] for x in l}
    # for x in l:
    #     if RepresentsInt(l[x]):
    #         yossi = int(l[x])
    #         if 'A' in x:
    #             playerA.append(yossi)
    #         else:
    #             playerB.append(yossi)
    if len(listA)==len(listB):
        sortA = listA.copy()
        sortB = listB.copy()
        #print ("origins", originA, originB)
        sortA.sort()
        sortB.sort()
        print("sort", sortA, sortB)
        if sortA == sortB:
            #print("hi", sortA, sortB)
            a,b,cp = BT(listA, listB)
            return render_template("answer.html", a=a, b=b, cp=cp)
        else:
            return render_template("error_elements.html")
    else:
        return render_template("error_len.html")


# app.run(debug=True)