# patient database
detail=[]

def add_patient():
    
    p_id=int(input("Enter the patient's ID : "))
    name=input("Enter the name of  THE Patient :").capitalize()
    age=int(input("Enter the age of the Patient :"))
    gender=input("enter the gender of the Patient : ").capitalize()
    contact=int(input("Enter the contact number of the Patient :"))

    med_hist={"Blood group":input("enter patient blood group :"),
              "Ongoing treatment":input("enter the previous disease treatment :"),
              "Recovery status":input("enter the recovery status of the Patient :")}
    
    d={"p_id":p_id,
       "name":name,
       "age":age,
       "gender":gender,
       "contact":contact,
       "med_hist":med_hist}
    
    detail.append(d)
    print("===PATIENT ADDED SUCCSSFULLY===")


def retrieve_info():

    info=int(input("enter the id of the Patient :"))
    for i in detail:
        if i["p_id"]==info:
            print("REQUIRED PATIENT'S INFORMATION :")
            print("patient id :",i["p_id"])
            print("name :",i["name"])
            print("age :",i["age"])
            print("gender :",i["gender"])
            print("contact :",i["contact"])
            print("med_hist :",i["med_hist"])


def update_history():
    info=int(input("enter the id of the Patient :"))
    for i in detail:
        if i["p_id"]==info:
            h1= input("enter patient blood group :")
            h2= input("enter the previous disease treatment :")
            h3= input("enter the recovery status of the Patient :")

            i["med_hist"]['Blood Group']=h1
            i["med_hist"]['Ongoing treatment']=h2
            i["med_hist"]['Recovery status']=h3


    print("====Medical histroy of patient updated====")

        
def display_info():
    for i in detail:
        print(f"\n{i['name']} details : \n"  )
        print("patient id :",i["p_id"])
        print("name :",i["name"])
        print("age :",i["age"])
        print("gender :",i["gender"])
        print("contact :",i["contact"])
        print("med_hist :",i["med_hist"],"\n")  


while True:
    print("\n------------PATIENT DATABASE---------------\n")
    print("1.add new patient")
    print("2.Retrieve patient information")
    print("3.update the medical history of the patient")
    print("4.Display information of all patients")
    print("5.Exit\n")
    ch=int(input("Enter your choice (1-5): "))


    if ch==1:
        add_patient()
    elif ch==2:
        retrieve_info()
    elif ch==3:
        update_history()
    elif ch==4:
        display_info()
    elif ch ==5:
        break
    else:
        print("Invalid choice. Please try again.")

            



    



             
    