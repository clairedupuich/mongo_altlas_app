import streamlit as st
from pymongo import MongoClient

#!上一个练习用了panda方法，此练习中用了pymong即mongolDB的python 方法建设APP
#!VScode 内部terminal打不开时，在外部打开一个 激活应用环境conda activate claierev 之后cd进入相应的文件夹并运行即可 streamlit run .\streamlit_car.py
    
# CONNECTION_STRING = 'mongodb+srv://claire:claire123@cluster0.74lta.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# client = MongoClient(CONNECTION_STRING)
client = MongoClient(**st.secrets['mongo'])
db = client.voiture
voiture = db.infor_voiture2


datasait_object = st.container()   
st.sidebar.title("select the makers to find the good car")
# choose car by maker
list_maker = voiture.distinct("Make") #distinct方法相当于pandas中的unique()方法，创造一个每个值只显示一次的名单list
list_model = voiture.distinct("Model")

search_by_maker = st.sidebar.selectbox("Search by Maker", list_maker)
# for i in list_maker:
#if search_by_maker == i 
# search_by_model= st.sidebar.selectbox("Search by Model",voiture.find({"Make":i},{"Model:1","_id:0"}))

if  search_by_maker:
    search_by_model = st.sidebar.selectbox("Search by Model",voiture.distinct('Model',{"Make":search_by_maker})) #!根据选择的Make显示相应的model并且不会重复显示

#affire les informations de voiture
    def show_infor(voiture):     #!通过函数建立一种显示模型
        return f"La {voiture['Make']} {voiture['Model']} {voiture['Vehicle Style']} de {voiture['Year']} a {voiture['Engine HP']} chevaux et {voiture['Engine Cylinders']} cylindres. Sa consommation sur autoroute est de {voiture['highway km/litre']} km au litre et de {voiture['city km/litre']} km au litre en ville."
    display_result = [show_infor(voiture) for voiture in voiture.find({'Make': search_by_maker, 'Model': search_by_model})]
    for i in display_result:
        st.write(i)



# car_maker = st.text_input("Make:")
#     car_model = st.text_input("Model:")
#     car_year = st.number_input("Year:")
#     car_ehp = st.number_input("Engine HP:")
#     car_ec = st.number_input("Engine Cylinders:")
#     button_sumbit = st.button('add car')
#     if button_sumbit:
#         new_car = {
#             'Make': car_maker,
#             'Model': car_model,
#             'Year': car_year,
#             'Engine HP': car_ehp,
#             'Engine Cylinders':car_ec
#         }
#         voiture.insert(new_car)
#         st.write("### your new is add")
#     a = voiture.find({'Make':'claire'},{'Make'})
#     for i in a:
#         st.write(f'# {i}')
        
        
st.title("write all of the informations for your new car " )
# with st.form(key='my_form'):
#     car_maker = st.text_input("Make:")
#     car_model = st.text_input("Model:")
#     car_year = st.number_input("Year:")
#     car_ehp = st.number_input("Engine HP:")
#     car_ec = st.number_input("Engine Cylinders:")
#     button_sumbit = st.form_submit_button(label='Submit')

# if button_sumbit:
#         # new_car = {
#         #     'Make': car_maker,
#         #     'Model': car_model,
#         #     'Year': car_year,
#         #     'Engine HP': car_ehp,
#         #     'Engine Cylinders':car_ec
#         # }
#         # voiture.insert(new_car)
#         st.write("### your new car is add")
# a = voiture.find({'Make':'goose'},{'Make'})
# for i in a:
#     st.write(f'# {i}')
    
form = st.form(key='my_form')
car_maker = form.text_input("Make:")
car_model = form.text_input("Model:")
car_year = form.number_input("Year:",min_value=1900, max_value=2022, step=1)
car_ehp = form.number_input("Engine HP:",min_value=1, max_value=1200, step=1)
car_ec = form.number_input("Engine Cylinders:",min_value=1, max_value=16, step=1)
submit_button = form.form_submit_button(label='Submit')
if submit_button:
        new_car = {
            'Make': car_maker,
            'Model': car_model,
            'Year': car_year,
            'Engine HP': car_ehp,
            'Engine Cylinders':car_ec
        }
        voiture.insert_one(new_car)
        st.write("### your new car is add")
a = voiture.find({'Make':'goose'})
for i in a:
    st.write(f'# {i}')