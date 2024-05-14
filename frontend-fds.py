import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)
icon = Image.open('Logo.png')

# Page config
st.set_page_config(page_title="Squad Predictor",
                     page_icon=icon      
                   )
st.image('Logo.png',width=500)
image_path = "C://Users//keane//OneDrive//Desktop//College//3rd year//FDS//Project//Logo.png"

# Function to load data based on position
def load_data(position):
    if position == 'Defensive':
        filepath = './Combined Data/Defenders_data_2023-24.csv'
    elif position == 'Goalkeeper':
        filepath = './Combined Data/Goalkeepers_data_2023-24.csv'
    elif position == 'Offensive':
        filepath = './Combined Data/Attackers_data_2023-24.csv'
    else:
        return pd.DataFrame()

    df = pd.read_csv(filepath)
    # Remove unwanted columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[:, ~df.columns.str.contains('^Born')]
    return df

# Function to generate comparison bar plots
def generate_comparison_plots(players_data, attributes):
    for attribute in attributes:
        plt.figure(figsize=(10, 6))
        for player_data in players_data:
            value = player_data[attribute]
            plt.bar(player_data['Player'], value, label=player_data['Player'])
        plt.xlabel('Player')
        plt.ylabel(attribute)
        plt.title(f'Comparison of Players on {attribute}')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        st.pyplot()

def main():
    comparison_mode = st.radio("Select Comparison Mode:",
                               ('Compare Players from Specific Country', 'Compare Any Players','Starting 11 Predictor'))

    
    if comparison_mode == 'Compare Players from Specific Country':
        st.title('Player Comparison from Specific Country')
        position = st.selectbox('Select Position:', ['Defensive', 'Goalkeeper', 'Offensive'])
        data = load_data(position)
        country = st.selectbox('Select Country:', data['Nation'].unique())
        top_attribute = st.selectbox('Select Attribute to Rank by:', sorted(data.columns))
        num_players = st.number_input('How many players do you want to compare?', min_value=1, max_value=len(data), value=10)

        top_players = data[data['Nation'] == country].nlargest(num_players, top_attribute).to_dict('records')
        generate_comparison_plots(top_players, [col for col in data.columns if col not in ['Player', 'Nation', 'Position']])

    elif (comparison_mode == "Compare Any Players"):  # Compare Any Players
        st.title('Player Comparison')
        position = st.selectbox('Select Position:', ['Defensive', 'Goalkeeper', 'Offensive'])
        data = load_data(position)
        num_players = st.number_input('How many players do you want to compare?', min_value=2, max_value=len(data), value=2)
        players_data = []
        for n in range(int(num_players)):
            player = st.selectbox(f'Player {n+1} Name:', sorted(data['Player'].unique()), key=f"player_{n}")  # Unique key for each selectbox
            player_data = data[data['Player'] == player].iloc[0].to_dict()
            players_data.append(player_data)

        attributes = st.multiselect('Select Attributes to Compare:', [col for col in data.columns if col not in ['Player', 'Nation', 'Position']])

        if st.checkbox('Compare selected players on all attributes'):
            attributes = [col for col in data.columns if col not in ['Player', 'Nation', 'Position']]

        if st.button('Compare Players'):
            generate_comparison_plots(players_data, attributes)
    elif (comparison_mode =="Starting 11 Predictor"):
        st.title("Euro 2024 Starting 11 ")
        st.write("""

        Predicts the squad for a Euro 2024 team based on the player's performance in the 2023/24 season.

        """)
        country = st.selectbox("Select the Country:",("ALB", "AUT", "BEL", "CRO", "CZE", "DEN", "ENG", "FRA", "GEO", "GER", "HUN", "ITA", "NED", "POL", "POR", "ROU", "SCO", "SRB", "SVK", "SVN", "ESP", "SUI", "TUR", "UKR"))
        att_no = st.selectbox("Number of Attackers:",(1,2,3,4))
        mid_no = st.selectbox("Number of Midfielders:",(2,3,4,5,6))
        def_no = st.selectbox("Number of Defenders:",(2,3,4,5))


        def attackers(country, att_no):
            df = pd.read_csv('./Performance Rating/Attackers_data.csv')
            df = df[df['Nation'] == country]
            df_sorted = df.sort_values(by='Performance_rating', ascending=False)
            st.write(df_sorted[['Player','Performance_rating']].head(att_no))


        def midfielders(country,mid_no):
            df = pd.read_csv('./Performance Rating/Midfielders_data.csv')
            df = df[df['Nation'] == country]
            df_sorted = df.sort_values(by='Performance_rating', ascending=False)
            st.write(df_sorted[['Player','Performance_rating']].head(mid_no))


        def defenders(country, def_no):
            df = pd.read_csv('./Performance Rating/Defenders_data.csv')
            df = df[df['Nation'] == country]
            df_sorted = df.sort_values(by='Performance_rating', ascending=False)
            st.write(df_sorted[['Player','Performance_rating']].head(def_no))

        def goalkeepers(country):
            df = pd.read_csv('./Performance Rating/Goalkeepers_data.csv')
            df = df[df['Nation'] == country]
            df_sorted = df.sort_values(by='Performance_rating', ascending=False)
            st.write(df_sorted[['Player','Performance_rating']].head(1))


        if st.button("Predict Squad", type="primary"):
            if(att_no + mid_no + def_no + 1 != 11):
                st.error("Please select the correct number of players")
            else:
                st.write("Attackers")
                attackers(country,att_no=att_no)
                st.write("Midfielders")
                midfielders(country,mid_no)
                st.write("Defenders")
                defenders(country,def_no)
                st.write("Goalkeeper")
                goalkeepers(country)
 
if __name__ == '__main__':
    main()
