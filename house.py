from flask import Flask,render_template,request
import pickle
import numpy as np


# 1.created object for class Flask
app=Flask(__name__)

# loading model--model should contain only numbers
with open("price_model.pkl","rb")as f:
    linear_regressor=pickle.load(f)

#7.
def predict_price(Square_Footage=1562,Num_Bedrooms =3,Num_Bathrooms=2,Lot_Size=0.524058,Garage_Size=1,Neighborhood_Quality=10):
    temp_array=list()
    
    #Square_Footage
    temp_array=temp_array +[Square_Footage]
    
    #Num_Bedrooms
    temp_array=temp_array +[Num_Bedrooms]

    #Num_Bathrooms
    temp_array=temp_array +[Num_Bathrooms]

     #Lot_Size
    temp_array=temp_array +[Lot_Size]

     #Garage_Size
    temp_array=temp_array +[Garage_Size]

     #Neighborhood_Quality
    temp_array=temp_array +[Neighborhood_Quality]


    #converting into numpy array
    temp_array= np.array([temp_array])
    print(temp_array)
    
    
    
    
    return int(linear_regressor.predict(temp_array))
# we have to make the previous model to our model name(ex=rfc.predict to---model.predict)



# 3.creating router
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html') 

@app.route("/properties")
def properties():
    return render_template('properties.html') 

# 4.
@app.route("/predict",methods=['POST','GET'])
#5. we have to check wheter form.get is string or number
def predict():
    if request.method=='POST':
        Square_Footage=int(request.form.get('Square_Footage'))
        Num_Bedrooms=int(request.form.get('Num_Bedrooms'))
        Num_Bathrooms=int(request.form.get('Num_Bathrooms'))
        Lot_Size=float(request.form.get('Lot_Size'))
        Garage_Size=int(request.form.get('Garage_Size'))
        Neighborhood_Quality=int(request.form.get('Neighborhood_Quality'))
        print(type(Square_Footage))
        price=predict_price(Square_Footage=Square_Footage,Num_Bedrooms =Num_Bedrooms,Num_Bathrooms=Num_Bathrooms,Lot_Size=Lot_Size,
                            Garage_Size=Garage_Size,Neighborhood_Quality=Neighborhood_Quality)
        print(price)
        return render_template('result.html',prediction=price)


    return render_template('predict.html') 

@app.route("/contact")
def contact():
    return render_template('contact.html') 



#2. to create main function
if __name__=='__main__':
    # running server
    app.run(debug=True,port=4000)

