
import math
import streamlit as st

def miles_above_mars(m: int):
    yards = m * 1760
    feet = m * 5280
    inches = m * 63360
    return f"Yards = {yards}, Feet = {feet}, Inches = {inches}"

def kilo_above_mars(k: int):
    meters = k * 1000
    centimeters = k * 100000
    millimeters = k * 1000000
    return f"Meters = {meters}, Centimeters = {centimeters}, Millimeters = {millimeters}"

def menu_1():
    conversion_choice = st.radio("Select conversion type:", ("Miles above Mars", "Kilometers above Mars"))

    if conversion_choice == "Miles above Mars":
        miles = st.number_input("Enter the amount of Miles", min_value=0, step=1, format="%d")
        if miles > 0:
            try:
                st.text(miles_above_mars(miles))
            except Exception as e:
                st.error(f"Error: {e}")

    elif conversion_choice == "Kilometers above Mars":
        kilometers = st.number_input("Enter the number of Kilometers", min_value=0, step=1, format="%d")
        if kilometers > 0:
            try:
                st.text(kilo_above_mars(kilometers))
            except Exception as e:
                st.error(f"Error: {e}")

# def menu():
#     most_efficent_pizza = 100
#     most_efficent_shape = "Nothing Yet"

#     while True:
#         user_choice = int(input(f"\n 1: Circle \n 2: Trianlge \n 3: Square \n 4: Most Effienct Pizza \n5: Quit \n Enter a choice: "))
#         if user_choice == 1:
#             area = area_of_circle(int(input("Enter in the Diameter:")))
#             effiency = compare(area)
#             if effiency <= most_efficent_pizza:
#                 most_efficent_pizza += effiency
#                 most_efficent_shape = "Circle"
#         if user_choice == 2:
#             area = area_of_triangle(int(input("Enter in a side: ")))
#             effiency = compare(area)
#             if effiency <= most_efficent_pizza:
#                 most_efficent_pizza += effiency
#                 most_efficent_shape = "Triangle"
#         if user_choice == 3:
#             area = area_of_square(float(input("Enter in a side: ")))
#             effiency = compare(area)
#             if effiency <= most_efficent_pizza:
#                 most_efficent_pizza += effiency
#                 most_efficent_shape = "Square"
#         if user_choice == 4:
#             print(f"The most effienct Shape: {most_efficent_shape} with an effiency of {most_efficent_pizza}")
#         if user_choice == 5:
#             break


def area_of_triangle(a:int) -> int:
    area = (math.sqrt(3) / 4) * a**2
    return area
def area_of_circle(d:int) -> int:
    area = (math.pi * d ** 2) / 4
    return area
def area_of_square(s:float) -> float:
    area = s**2
    return area

def calculate_efficiency(area: float, units_of_dough: float) -> float:
    if units_of_dough <= 0:
        return float('inf')
    return area / units_of_dough


def pizza_efficiency_app():

    if "most_efficient_pizza" not in st.session_state:
        st.session_state.most_efficient_pizza = float('inf')
        st.session_state.most_efficient_shape = "Nothing Yet"

    shape = st.selectbox("Choose pizza shape:", ["Circle", "Triangle", "Square"])

    units_of_dough = st.number_input("Enter units of dough:", min_value=0.01, step=0.01, format="%.2f")

    area_input = None
    if shape == "Circle":
        diameter = st.number_input("Enter Diameter:", min_value=0, step=1)
        area_input = area_of_circle(diameter)
    elif shape == "Triangle":
        side = st.number_input("Enter side length:", min_value=0, step=1)
        area_input = area_of_triangle(side)
    elif shape == "Square":
        side = st.number_input("Enter side length:", min_value=0.0, step=0.1, format="%.2f")
        area_input = area_of_square(side)

    if st.button("Calculate Efficiency"):
        if area_input is None or area_input == 0:
            st.warning("Please enter a valid dimension greater than 0.")
        elif units_of_dough <= 0:
            st.warning("Units of dough must be greater than 0.")
        else:
            efficiency = calculate_efficiency(area_input, units_of_dough)
            st.write(f"Efficiency for {shape}: {efficiency:.4f}")

            if efficiency < st.session_state.most_efficient_pizza:
                st.session_state.most_efficient_pizza = efficiency
                st.session_state.most_efficient_shape = shape
                st.success(f"🎉 New most efficient pizza: {shape} with efficiency {efficiency:.4f}")

    if st.button("Show Most Efficient Pizza"):
        if st.session_state.most_efficient_shape == "Nothing Yet":
            st.info("No pizza calculated yet.")
        else:
            st.write(f"Most efficient pizza so far is **{st.session_state.most_efficient_shape}** with efficiency {st.session_state.most_efficient_pizza:.4f}")

# empty_list = []


# def fuel_required(mass:int) -> int:
#     requirement =  math.floor((mass / 3)) - 2
#     return requirement


# # with open("./input.txt", "r") as file:
# #     for line in file:
# #         num_line = int(line)
# #         fuel_required(num_line)
# #         empty_list.append(num_line)

# total = sum(empty_list)

# print(total)

st.title("Multi-App")

if "page" not in st.session_state:
    st.session_state.page = None


if st.button("Conversion Button"):
    st.session_state.page = "conversion"

if st.button("Pizza Button"):
    st.session_state.page = "pizza"

# if st.button("Fuel Button"):
#     st.session_state.page = "fuel"

# Render content based on selected page
if st.session_state.page == "conversion":
    st.subheader("Conversion App")
    menu_1() 

elif st.session_state.page == "pizza":
    st.subheader("Pizza")
    pizza_efficiency_app()  # Call the pizza app

elif st.session_state.page == "fuel":
    st.subheader("Fuel")
    # Assuming 'total' is defined somewhere
    st.subheader(total)

else:
    st.write("Select an option by clicking a button above.")

