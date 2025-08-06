import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="VitaAssist",
    page_icon="❤️",
    layout="wide"
)

# --- Load Custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- Blood Test Data ---
BLOOD_TESTS = {
    "Complete Blood Count (CBC)": "A general test that helps detect anemia, infection, and several nutrient deficiencies, especially iron, B12, and folate.",
    "Vitamin D Test": "Measures 25-hydroxyvitamin D. Essential for bone health and immune support. Deficiency is linked to fatigue and depression.",
    "Vitamin B12 Test": "Critical for red blood cell production and nerve health. Deficiency may cause weakness or memory loss.",
    "Iron Studies": "Includes serum iron, TIBC, and ferritin. Helps detect anemia and chronic fatigue.",
    "Folic Acid (Vitamin B9) Test": "Vital during pregnancy. Low folate can cause weakness and fatigue.",
    "Calcium Test": "Necessary for muscle function, bone health, and nerve transmission.",
    "Magnesium Test": "Vital for energy production and muscle function. Deficiency may lead to muscle cramps and anxiety.",
    "Zinc Test": "Supports immunity, wound healing, and DNA synthesis.",
    "Thyroid Panel (TSH, T3, T4)": "Regulates metabolism. Imbalance can affect energy, weight, and mood.",
    "Lipid Profile": "Reflects overall metabolic health and nutrient processing, especially fat-soluble vitamins."
}

# --- Page Implementations ---
def home_blood_collection():
    st.header("Book Home Blood Collection 💉")
    st.markdown("Select the tests you need and schedule a home visit at your convenience.")
    
    with st.form("booking_form"):
        st.text_input("Full Name")
        st.text_input("Mobile Number")
        st.text_area("Address")
        
        selected_tests = st.multiselect("Choose Blood Tests:", options=list(BLOOD_TESTS.keys()))
        
        col1, col2 = st.columns(2)
        with col1:
            st.date_input("Preferred Date")
        with col2:
            st.time_input("Preferred Time")
            
        submitted = st.form_submit_button("Book Appointment")
        if submitted:
            st.success("Appointment booked successfully!")

def test_descriptions():
    st.header("Blood Test Descriptions 📖")
    st.markdown("Learn more about the nutrient-related blood tests we offer.")
    
    for test_name, description in BLOOD_TESTS.items():
        with st.expander(f"{test_name}"):
            st.write(description)

def contact_us():
    st.header("Contact Us ☎️")
    st.markdown("Find contact numbers for our centers or dial them directly.")
    
    location = st.selectbox("Choose a location:", ["New York", "Los Angeles", "Chicago", "San Francisco", "Miami"])
    
    if location:
        st.info(f"Contact number for {location}: +1-800-555-VITA")
        st.button(f"Dial for {location}")

def ai_nutritionist():
    st.header("AI Nutritionist Assistant 🤖")
    st.markdown("Upload your blood report to get a personalized diet plan from our AI assistant.")
    
    st.selectbox("Select LLM Model", ["Vita-GPT-4o", "Vita-Claude-3", "Vita-Gemini-Pro"])
    st.file_uploader("Upload your latest blood report (PDF, JPG, PNG)", type=['pdf', 'jpg', 'png'])
    
    if st.button("Get Diet Help"):
        with st.spinner("Our AI Nutritionist is analyzing your report..."):
            st.success("Analysis complete!")
            st.text_area("Your Personalized Diet Plan", "Based on your report, we recommend incorporating more leafy greens for iron, and consuming fatty fish for Vitamin D...", height=300)

# --- Main App Logic ---
def login_page():
    st.title("VitaAssist Login ❤️")
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="admin")
        password = st.text_input("Password", type="password", placeholder="admin")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username == "admin" and password == "admin":
                st.session_state["logged_in"] = True
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Incorrect username or password")

def main_application():
    load_css('style.css')
    st.sidebar.title("VitaAssist ❤️")
    
    with st.sidebar:
        selected_page = st.radio(
            "Main Menu",
            ["Home Blood Collection", "Test Descriptions", "Contact Us", "AI Nutritionist"],
        )
        st.success("You are logged in as 'admin'.")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

    if selected_page == "Home Blood Collection":
        home_blood_collection()
    elif selected_page == "Test Descriptions":
        test_descriptions()
    elif selected_page == "Contact Us":
        contact_us()
    elif selected_page == "AI Nutritionist":
        ai_nutritionist()

# --- App Entry Point ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main_application()
else:
    load_css('style.css') 
    login_page()
