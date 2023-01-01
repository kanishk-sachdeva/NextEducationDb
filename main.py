from flask import Flask, render_template, request,redirect,flash

app = Flask(__name__,template_folder='templates')

data = {
  "type": "service_account",
  "project_id": "sachdevadb1",
  "private_key_id": "5bf4165101211adf6893471a9bcf1bb260aa3471",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC72dmDOGegUTBb\nK2SszKaOVQpnNAXK2pYwk7IMd3lErPG5Spj4Kzmd64sE6N+QIS2XB8Iefu6/ZNHF\nc8TcruUaXumdv7+LcLFjPvSLr7RCXAe7mukyINO0gcGHDfriSY6ssom9Xb0cBhsS\nT32VXs1VvZ9NcddNjGFS38Pud46dpREwVUsw2g85X2nnjT3AevB09S4FcdrrNCmO\nDKp2iCy3Qg14FQhv+lB4rDOg8NJuyJA3SswNZbVkdSYiAHDoGn8mnx3yhejd7y3t\nvfki8qk8SY6AWIulyzjfhYVQIYbXSNHHXkXH0y8iD4l2T6r7/oP9FuCuCNnDCOAR\nib3UnDFxAgMBAAECgf9uIN7Ozy1GulJfIKbPp4BTHAgSo60W/+SNFgmMGtQ9hCaH\n5UlI32PSnAR5xwyfXX7HdwTsW/4cDD9EQwVmsMzKaQUM4R1VN6bHSGFAg1cVOwmi\n3W6utLq+Av7c7pU8P2N7BjCPlCUKCN+rccQY4ztTc5exD3c/P3gkiIrq2FdZPitE\nfp21kEPBW2Wq8to0dInFMG3wPQKRvgApSWVxKHea/XzvyRzbpNfzxMKyVP7D+Gvp\nba15ngotr7IoW0qRjo2GgiSCGz6AjfzOw2qPCNLQO9fLPWoPAYNq8uQH/zpLZBE8\nJM4M2n6xWg9XtAmO+wYdjPsysgKP6rN5tGqUWwECgYEA49yD/zzSrlEWdNeMyblY\nMrrexHbutKTfJCy0fUwAStuP2IM/btZVQPHlCD2zsaJCVOHpxQoSZWZhgImf5Dpy\nnHqXnSXBq90g8Oc4jdR7Q1g3s6eil5SDY+XsoWOZ0wkSwex5pRXjcWZBJ5jdLeLP\njxfi0enOp1HXgYvfi8L85rECgYEA0wx3hL9FiidUx4jNY7Qq/0v3FZ3cpUCkgH+z\nDMszvwKS6wZHFpVef4N1pI2U7geSkEB0ofi66NxJl1zfJOY0HanK8qDYj4uYqv6z\nqQQRQXo3rrwkCydy67S46jZaDyID+pptKNJb+jUseftqu8NwxUF4Hx158uQrYGll\nlTn0JsECgYEAitZGJzLsPAJ0aGUeB5vDPcXXDmZZNABxZh1HLEEuvG3jy8zMzcAS\n2iuJnefaoZV4TTgJtGFarCYhqqwwnGNwih+4WawzwYBPHfoE34ZkRLhv2CuASlPX\navshn4SMqaWRpE9uH0Si/OmNMY9W1SqpxUqMjdKkdBbN9MVBRGtepUECgYEAjUfr\nOpJQmwt5VZne5L/XiM/xuCbVbkq31M2nrwjYuyWd9HdfX17ew73dIyskZ7PqCWcc\nrNE1Tm0pVop1Vt5ERRdFJOdIEdABg3a+DocKhiqq2+5WsqDV7bQtlZyM7VR4FWsL\naChqKjUucPo9mTRcabBKGYpB+LeF0iS8PAlvyAECgYB8ZSkECCGfcDIM1E1w+vNT\nnBAn0VNlR0/dERk5YwSd6jFCs9XTuRK7PYLCy5Mr+Vk0vaR6GkQjRN8wNtG3enrh\nklElOaNgtWwXK5OgR4ma8nzquPMd6F046NNijgOoJjG+95K9Bx5zXB8acr13/WSV\nx/PcXbvnyGVQJgRGImg7bQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-hs539@sachdevadb1.iam.gserviceaccount.com",
  "client_id": "105003662047886903922",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-hs539%40sachdevadb1.iam.gserviceaccount.com"
}

import string
import random

N = 7

import firebase_admin,pymongo
from firebase_admin import credentials,storage

cred = credentials.Certificate(data)
firebase_admin.initialize_app(cred,{
    'storageBucket': 'sachdevadb1.appspot.com/'
})

bucket = storage.bucket("sachdevadb1.appspot.com")

myclient = pymongo.MongoClient("mongodb+srv://kanu00047:Theindian%2337@cluster0.dizvk.mongodb.net")
mydb = myclient["students"]["certificates"]

@app.route('/adminupload')
def update_user():
    return render_template('adminupload.html')

@app.route('/secureupload', methods=['GET', 'POST'])
def secure_upload():
    if request.method == 'POST':

        if request.form.get('adminid', "") == "9988591098":
            studentphotorequest = request.files['studentphoto']

            studentname = request.form.get("studentname", "")
            studentfathername = request.form.get("studentfathername", "")
            studentmothername = request.form.get("studentmothername", "")
            coursename = request.form.get("coursename", "")
            studentdob = request.form.get("studentdob", "")
            coursestartdate = request.form.get("coursestartdate", "")
            courseduration = request.form.get("courseduration", "")
            obtainedmarks = request.form.get("obtainedmarks", "")
            studentid = request.form.get("studentid", "")

            res = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=N))
            filexte = studentphotorequest.filename[-12:]
            filexte = filexte.replace(" ", "")
            blob = bucket.blob(str(res) + filexte)
            blob.upload_from_file(studentphotorequest)
            blob.make_public()
            photopublicurl = blob.public_url

            post_data = {
                "studentid": "{}".format(studentid),
                "studentphoto": "{}".format(photopublicurl),
                "studentname": "{}".format(studentname),
                "studentfathername": "{}".format(studentfathername),
                "studentmothername": "{}".format(studentmothername),
                "studentdob": "{}".format(studentdob),
                "coursename": "{}".format(coursename),
                "coursestartdate": "{}".format(coursestartdate),
                "courseduration": "{}".format(courseduration),
                "obtainedmarks": "{}".format(obtainedmarks),
            }

            myquery = {"studentid": studentid}
            mydoc = mydb.find_one(myquery)

            # newvalues1 = {"$set": {"image_link": blob.public_url}}
            newvalues1 = {"$set": post_data}

            if mydoc == None:
                h = mydb.insert_one(post_data)
                mongoid = h.inserted_id


            else:
                y = mydb.update_one(myquery, newvalues1)
                mongoid = mydoc.get('_id')

            mongoid = str(mongoid)

            errormsg = [{
                'alertcode': 'success',
                'mongoid': mongoid,
                'backlink': '/adminupload',
                'returnbacktext': 'Return Back and Upload new Userdata',
                'alerth1': 'Data has been successfully uploaded/updated to database with id : ' + mongoid,
                'alertp': 'Certificate Successfully created/updated with following Credentials and share it with your student Student id : ' + studentid + ' and Password(DOB) : ' + studentdob,
                'alertheading': 'Successfully Uploaded the Student Certificate with Roll number ' + studentid,
            }]

            return render_template('alertpage.html', data=errormsg)

        else:
            errormsg = [{
                'alertcode': 'danger',
                'backlink': '/adminupload',
                'returnbacktext': 'Return Back and Try Again !!',
                'alerth1': '',
                'alertp': 'Please contact admin of this website to recheck your admin id once again.',
                'alertheading': 'Error ! Admin Id was wrong',
            }]
            return render_template('alertpage.html', data=errormsg)







    else:
        return redirect('https://nexteducationfdk.com', code=302)


@app.route('/getuser', methods=['GET', 'POST'])
def get_user():

    if request.method == 'POST':
        studentid = request.form.get("studentid","")
        studentpass = request.form.get("studentpassword","")

        myquery = {"studentid": studentid}
        mydoc = mydb.find_one(myquery)

        if mydoc != None:
            if str(mydoc.get('studentdob')).lower() == str(studentpass).lower():
                data = [{
                    'studentphoto': mydoc.get('studentphoto'),
                    'studentid': mydoc.get('studentid'),
                    'studentname': mydoc.get('studentname'),
                    'studentfathername': mydoc.get('studentfathername'),
                    'studentmothername': mydoc.get('studentmothername'),
                    'coursename': mydoc.get('coursename'),
                    'courseduration': mydoc.get('courseduration'),
                    'coursestartdate': mydoc.get('coursestartdate'),
                    'obtainedmarks': mydoc.get('obtainedmarks'),
                }]

                return render_template('studentdata.html', data=data)

            else:
                data = [{
                    'errorstatus': 'Oops ! Your Password means DOB is wrong ! Try again',
                }]
                return render_template('studentdata.html', data1=data)



        else:
            data = [{
                'errorstatus': 'No Student found with this Student id !!',
            }]
            return render_template('studentdata.html', data1=data)




    else:
        return render_template('studentdata.html')

@app.route('/all', methods=['GET', 'POST'])
def all_users():
    if request.method == "POST":
        passcode = request.form.get("passcode","")
        if passcode == "9988591098":
            users = []
            cursor = mydb.find({})
            n = 0
            for document in cursor:
                student = {}
                n = n + 1
                student['id'] = "{}".format(n)
                student['studentid'] = document.get("studentid")
                student['studentphoto'] = document.get("studentphoto")
                student['studentname'] = document.get("studentname")
                student['studentfathername'] = document.get("studentfathername")
                student['studentmothername'] = document.get("studentmothername")
                student['studentdob'] = document.get("studentdob")
                student['coursename'] = document.get("coursename")
                student['coursestartdate'] = document.get("coursestartdate")
                student['courseduration'] = document.get("courseduration")
                student['obtainedmarks'] = document.get("obtainedmarks")

                users.append(student)
            return render_template('allusers.html', users=users, login=[{}])
        else:
            return render_template('allusers.html', signin=[{}], error=[{}])

    else:
        return render_template('allusers.html', signin=[{}])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
