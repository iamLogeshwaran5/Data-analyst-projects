import pandas as pd
import streamlit as st

# Function to load the dataset
def load_data():
    return pd.read_csv(r"D:/project/Python Data analysis Hands project/project-1/Weather_Dataset.csv")

st.markdown("<h1 style='color: white; border: 2px solid yellow; padding: 5px; text-align: center;'>Weather Data Analysis</h1>", unsafe_allow_html=True)
# Function to set background image
def setting_bg(background_url):
        st.markdown(f""" 
        <style>
            .stApp {{
                background: url("{background_url}");
                background-size: cover
            }}
        </style>
    """, unsafe_allow_html=True)

# Load the dataset
data = load_data()

# Define background images
background_images = {
    'Unique Wind Speed values': 'https://i.pinimg.com/originals/e4/a8/b8/e4a8b8817c453d28b22fe88f330479eb.gif',
    'Number of times Weather is exactly Clear': 'https://www.aopa.org/-/media/Images/AOPA-Main/News-and-Media/Publications/Flight-Training-Magazine/2010f/2010f_pf_wx/2010f_pf_wx_16x9.jpg?h=675&w=1200&la=en&hash=AEE0F0F385D41A869832D85F72B45DBA',
    'Number of times Wind Speed was exactly 4 km/h': 'https://scitechdaily.com/images/Wind-Farm.gif',
    'Null Values in the data': 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg',
    "Renamed column 'Weather' to 'Weather Condition'": 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg',
    'Mean Visibility': 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg',
    'Standard Deviation of Pressure': 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg',
    'Variance of Relative Humidity': 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg',
    'Instances when "Snow" was recorded': 'https://i.pinimg.com/originals/aa/28/72/aa287235fd452fc155cb662ffd2ef045.gif',
    'Instances when "Wind Speed is above 24" and "Visibility is 25"': 'https://scitechdaily.com/images/Wind-Farm.gif',
    'Min & Max value of each column against each "Weather"': 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg',
    'Records where Weather is Fog': 'https://i.pinimg.com/originals/03/53/cd/0353cdf9b3b43ea8e16506cde3ec94ef.gif',
    'Instances when "Weather is Clear" or "Visibility is above 40"': 'https://www.aopa.org/-/media/Images/AOPA-Main/News-and-Media/Publications/Flight-Training-Magazine/2010f/2010f_pf_wx/2010f_pf_wx_16x9.jpg?h=675&w=1200&la=en&hash=AEE0F0F385D41A869832D85F72B45DBA',
    'Instances When "Weather is Clear" and "Relative Humidity is greater than 50" or "Visibility is above 40"': 'https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700440706.jpg'
}

# Select box to choose the question
selected_option = st.selectbox("Select Question", list(background_images.keys()))

# Add background image based on the selected option
if selected_option in background_images:
    setting_bg(background_images[selected_option])

# Process the selected option
if selected_option == 'Unique Wind Speed values':
    st.write("### Unique Wind Speed values")
    unique_wind_speeds = data['Wind Speed_km/h'].unique()
    unique_wind_speeds_str = ', '.join(map(str, unique_wind_speeds))
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{unique_wind_speeds_str}</div>', unsafe_allow_html=True)

elif selected_option == 'Number of times Weather is exactly Clear':
    st.write("### Number of times Weather is exactly Clear")
    clear_weather_count = data[data['Weather'] == 'Clear'].shape[0]
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{clear_weather_count}</div>', unsafe_allow_html=True)

elif selected_option == 'Number of times Wind Speed was exactly 4 km/h':
    st.write("### Number of times Wind Speed was exactly 4 km/h")
    wind_speed_4_count = data[data['Wind Speed_km/h'] == 4].shape[0]
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{wind_speed_4_count}</div>', unsafe_allow_html=True)

elif selected_option == 'Null Values in the data':
    st.write("### Null Values in the data")
    null_values = data.isnull().sum()
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{null_values}</div>', unsafe_allow_html=True)

#elif selected_option == "Renamed column 'Weather' to 'Weather Condition'":
    st.write("### Renamed column 'Weather' to 'Weather Condition'")
    data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{data}</div>', unsafe_allow_html=True)

elif selected_option == 'Mean Visibility':
    st.write("### Mean Visibility")
    mean_visibility = data['Visibility_km'].mean()
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{mean_visibility}</div>', unsafe_allow_html = True)

elif selected_option == 'Standard Deviation of Pressure':
    st.write("### Standard Deviation of Pressure")
    pressure_std = data['Press_kPa'].std()
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{pressure_std}</div>',
                unsafe_allow_html=True)

elif selected_option == 'Variance of Relative Humidity':
    st.write("### Variance of Relative Humidity")
    humidity_variance = data['Rel Hum_%'].var()
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{humidity_variance}</div>',
                unsafe_allow_html=True)

elif selected_option == 'Instances when "Snow" was recorded':
    st.write("### Instances when 'Snow' was recorded")
    snow_instances = data[data['Weather'].str.contains('Snow')]
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{snow_instances}</div>',
                unsafe_allow_html=True)

elif selected_option == 'Instances when "Wind Speed is above 24" and "Visibility is 25"':
    st.write("### Instances when 'Wind Speed is above 24' and 'Visibility is 25'")
    instances_wind_speed_visibility = data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
    st.markdown(
        f'<div style="background-color:#000000; color:white; padding:10px">{instances_wind_speed_visibility}</div>',
        unsafe_allow_html=True)

elif selected_option == 'Min & Max value of each column against each "Weather"':
    st.write("### Min & Max value of each column against each 'Weather")
    min_max_by_weather_condition = data.groupby('Weather').agg(['min', 'max'])
    st.markdown(
        f'<div style="background-color:#000000; color:white; padding:10px">{min_max_by_weather_condition}</div>',
        unsafe_allow_html=True)

elif selected_option == 'Records where Weather is Fog':
    st.write("### Records where Weather is Fog")
    fog_records = data[data['Weather'] == 'Fog']
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{fog_records}</div>',
                unsafe_allow_html=True)

elif selected_option == 'Instances when "Weather is Clear" or "Visibility is above 40"':
    st.write("### Instances when 'Weather is Clear' or 'Visibility is above 40'")
    clear_or_high_visibility_instances = data[(data['Weather'] == 'Clear') | (data['Visibility_km'] > 40)]
    st.markdown(
        f'<div style="background-color:#000000; color:white; padding:10px">{clear_or_high_visibility_instances}</div>',
        unsafe_allow_html=True)

elif selected_option == 'Instances When "Weather is Clear" and "Relative Humidity is greater than 50" or "Visibility is above 40"':
    st.write(
        "### Instances When 'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40'")
    filtered_data = data[((data['Weather'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]
    st.markdown(f'<div style="background-color:#000000; color:white; padding:10px">{filtered_data}</div>',
                unsafe_allow_html=True)

# About Developer Section
developer_details = """
    ### About Developer
    - **Name:** John Doe
    - **LinkedIn:** [Linkedin Profile](https://www.linkedin.com/in/johndoe)
    - **GitHub:** [GitHub Profile](https://github.com/johndoe)
    - **Email:** john.doe@example.com
    """

# Background banner
st.markdown(
    """
    <style>
        .banner {
            background-image: url('https://i.pinimg.com/564x/08/34/01/0834012b52533eef29f68e21b05e3e90.jpg');
            background-size: 20000px 10000px;
            padding: 50px;
            color: red;
            text-align: center;
        }
        .developer-details {
            padding: 20px;
            color: black;
        }
    </style>
    <div class="banner">
        <div class="developer-details">
            <h1 style="color: red;">Developer Details</h1>
            <p>Name: Logeshwaran C</p>
            <p>LinkedIn: <a href="https://www.linkedin.com/in/logeshwarandatapro">Linkedin Profile</a></p>
            <p>GitHub: <a href="https://github.com/iamLogeshwaran5">GitHub Profile</a></p>
            <p>Email: logeshwaran1478@gmail.com</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
