# SJC-Consultancy
This is a Repo for the Fundamental of Data Science (FDS) project. Contains all the necessary code files and the data required to replicate the Git Hub.
### Frontend 
Check out the working app: https://sjc-consultancy-run.streamlit.app/

### To Replicate this code 

```
git clone https://github.com/keanec27/SJC-Consultancy.git
```
Install required python modules
```
pip install -r requirements.txt
```
Run the Streamlit App
```
streamlit run frontend-fds.py
```

### File Descriptions 

`Attackers Data`: Contains attacker data of the 5 Major leagues.

`Defenders Data`: Contains defender data of the 5 Major leagues.

`Goalkeepers Data`: Contains goalkeeper data of the 5 Major leagues.

`Combined Data`: Contains the Combined data of the above mentioned folders.

`Performance Rating`: Contains the datasets after performance rating has been calculated.

`AFCON_predictions.ipynb`: Contains Match and Tournament Simulation of the recently concluded CAF Africa Cup of Nations 2023 using Poisson Regression.

`AFC_Asian_Cup_predictions.ipynb`: Contains Match and Tournament Simulation of the recently concluded AFC Asian Cup 2023 using Poisson Regression.


`Dataset Combine.ipynb`: Jupyter notebook where all the data was combined.

`PL Player Stats - Scraping Bot.ipynb`: Web Scraping Script to get data from fbref.com , Incase data of another league is needed change the date accordingly.

'Performance Models.ipynb` : Performance models are calculated in this notebook.

`frontend-fds.py` : Contains the code for the Streamlit app.





