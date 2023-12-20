from flask import Flask , request , render_template
import os
import sqlite3



app = Flask(__name__)

picFolder = os.path.join('static' ,'pics')

app.config['UPLOAD_FOLDER'] = picFolder


@app.route("/home")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'] , 'bus-animation2.gif')
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')    
    return render_template("land.html" , image = pic1  , logo = logo)

@app.route("/success")
def success():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    image = os.path.join(app.config['UPLOAD_FOLDER'] , 'thanks.png')
    return render_template("success.html" , image = image , logo = logo  )

@app.route("/search")
def search():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'] , 'service.png')
    return render_template("search.html" , image = pic1 , logo = logo )

@app.route("/result")
def result():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    bus = os.path.join(app.config['UPLOAD_FOLDER'] , 'bus.png')
    return render_template("result.html" , bus = bus , logo = logo )

@app.route("/add")
def add():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'] , 'add.png')
    return render_template("add.html" ,image = pic1 , logo = logo)

@app.route("/about")
def about():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    info = os.path.join(app.config['UPLOAD_FOLDER'] , 'info.png')
    return render_template("about.html" , info = info , logo = logo )

@app.route("/details")
def details():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'] , 'service.png')
    return render_template("details.html" , image = pic1 , logo = logo )

@app.route("/footer")
def footer():
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    phone = os.path.join(app.config['UPLOAD_FOLDER'] , 'phone.png')
    email = os.path.join(app.config['UPLOAD_FOLDER'] , 'email.png')
    facebook = os.path.join(app.config['UPLOAD_FOLDER'] , 'facebook.png')
    twitter = os.path.join(app.config['UPLOAD_FOLDER'] , 'twitter.png')
    insta = os.path.join(app.config['UPLOAD_FOLDER'] , 'insta.png')
    return render_template("footer.html" , phone = phone , logo = logo , email = email , facebook = facebook , twitter = twitter , insta = insta  )



@app.route("/select" , methods=["POST" , "GET"])
def select():
    from_d = request.form.get("from")
    to_d = request.form.get("to")
    num = request.form.get("num")
    conn = sqlite3.connect("database/buses.db")
    cur = conn.cursor()
    if num != "" :
        cur.execute(f"""SELECT Bus_nm , Direction
  FROM buses where Direction Like '{from_d}%' and Direction Like '%{to_d}%' and Bus_nm = {num};
                
                    """)
    else:
      cur.execute(f"""SELECT Bus_nm , Direction
  FROM buses where Direction Like '{from_d}%' and Direction Like '%{to_d}%';
                
                    """)
           
        
    
    conn.commit()
    result = cur.fetchall()
    

    len(result)
    conn.close()
    logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
    bus = os.path.join(app.config['UPLOAD_FOLDER'] , 'bus.png')
    finalResult=[]
    for i in range(len(result)):
        d = {"busNumber" : result[i][0] , "busDirc" : result[i][1] }
        finalResult.append(d)
    leng = len(result)
    return render_template("result.html" , bus = bus , logo = logo , result = finalResult , leng = leng , from1 = from_d , to1 = to_d , num = num )




@app.route("/post" , methods=["POST" , "GET"])
def post():
    direct = request.form.get("direc")
    num = request.form.get("num")
    conn = sqlite3.connect("database/buses.db")
    cur = conn.cursor()
    cur.execute(f"""SELECT Bus_nm 
  FROM buses where Bus_nm = {num};            
                    """)

           
        
    
    conn.commit()
    result = cur.fetchall()
    print(result)
    
    if result == []:
      cur.execute(f"""INSERT INTO buses (
                      Direction,
                      Bus_nm
                  )
                  VALUES (
                      '{direct}',
                      '{num}'
                  );
                  """)
    
      conn.commit()
      conn.close()
      logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
      image = os.path.join(app.config['UPLOAD_FOLDER'] , 'thanks.png')
      return render_template("success.html" , image = image , logo = logo  )
    else:
        logo = os.path.join(app.config['UPLOAD_FOLDER'] , 'logo.png')
        image = os.path.join(app.config['UPLOAD_FOLDER'] , 'failed.png')
        return render_template("failed.html" , image = image , logo = logo  )
        
      
      
    
    
    
    
    













if __name__ == "__main__":
    app.run(debug=True )
