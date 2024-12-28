import pickle
import streamlit  as st


model=pickle.load(open("C:/Users/dongm/Desktop/Desktop/LEPRINCE/UDEMY DATA CAR PREDICTED/random_forest_model.pkl","rb"))

def main():
    st.title("Car Pricing Prediction Solution")
    
    #input variable
    year=st.text_input("year")
    Present_Price =st.text_input("Present_Price")
    Kms_Driven =st.text_input("Kms_Driven")
    Owner =st.text_input("Owner")
    Fuel_Type_Diesel =st.text_input("Fuel_Type_Diesel")
    Fuel_Type_Petrol =st.text_input("Fuel_Type_Petrol")
    Seller_Type_Individual =st.text_input("Seller_Type_Individual")
    Transmission_Manual =st.text_input("Transmission_Manual")


# prediction code
    if st.button("Predict"):  # Utilisez bien st.button en minuscule
        try:
            # Conversion des valeurs d'entrée
            year = int(year)
            Present_Price = float(Present_Price)
            Kms_Driven = float(Kms_Driven)
            Owner = int(Owner)
            Fuel_Type_Diesel = int(Fuel_Type_Diesel)
            Fuel_Type_Petrol = int(Fuel_Type_Petrol)
            Seller_Type_Individual = int(Seller_Type_Individual)
            Transmission_Manual = int(Transmission_Manual)

            # Faire la prédiction
            make_prediction = model.predict([[year, Present_Price, Kms_Driven, Owner,
            Fuel_Type_Diesel, Fuel_Type_Petrol, 
            Seller_Type_Individual, Transmission_Manual]])

            # Extraction du résultat de prédiction
            output = make_prediction[0]
            st.success("You can sell your car for ${:.2f}".format(output))

        except ValueError:
            st.error("Please enter valid input values.")
if __name__=="__main__":
    main()   