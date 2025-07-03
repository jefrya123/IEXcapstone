import streamlit as st

st.set_page_config(page_title="Titanic Dashboard")
st.title("Titanic Dashboard")
st.subheader("Welcome to the Titanic Dashboard")

st.markdown("""
Use the sidebarod to 
- **View Passenger List**: See all passengers on the Titanic.
- **Add Passenger**: Add a new passenger to the list.
- **Update Passenger**: Modify details of an existing passenger.
- **Visualize Data**: Explore visualizations of the Titanic data.
""")            