from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/form', methods=['GET', 'POST'])
def login():
        return render_template("login.html")


@app.route('/result/', methods=['GET','POST'])
def result():
    if request.method=="POST":
        res=request.form
        dob=res.get("dob")
        designation=res.get("designation")
        fname=res.get("fname")
        lname=res.get("lname")
        address=res.get("address")
        phoneno=res.get("phoneno")
        Education=res.get("Education")
        skills=res.get("skills")
        certificates=res.get("certificates")
        lang=res.get("lang")
        email=res.get("email")
        country=res.get("country")
        hobbies=res.get("hobbies")
        project=res.get("project")
        github=res.get("github")
        linkedIn=res.get("linkedIn")
        summary=res.get("summary")


        return render_template("download.html",res=res,dob=dob,fname=fname,lname=lname,address=address,phoneno=phoneno,Education=Education,skills=skills,
                               lang=lang,country=country,github=github,certificates=certificates,linkedIn=linkedIn,email=email,hobbies=hobbies,project=project,summary=summary,designation=designation)


    else:
        return "test nainu here "


