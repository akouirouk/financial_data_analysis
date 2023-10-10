# Financial Data Analysis
I will be analyzing the dataset [available on Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1/) which contains a CSV file of simulated mobile money transactions. 

The simulated data is derived from a sample of real transactions from a month of financial logs from a mobile money service based in an African country. 

## Goal
**Create a PDF document for a group Compliance Mangers containing:**
1. A write-up of methodology explaining how you:
       a. Validated and cleaned the data
       b. Explored trends or patterns in the data
       c. Decided on which insights to highlight from the data (rank importance of highlights)
       d. What additional information/context could have been useful in forming the conclusion
2. Key insights and trends from dataset
       a. Identify patterns of interest or trends over time that could have significant business impact or impact on Compliance policy or operational practices
       b. Include visualizations (graphs, pie charts, pivot tables, etc.)
4. Executive Summary
        a. Summarize insights and their implications for Compliance Operations and testing and optimization of teams

## Necessary Steps
1. Import dataset into Pandas DataFrame using Python
2. Validate and clean the data using Pandas 
3. Create MySQL table and insert records into table
4. Analyze the data via Python, SQL, and Tableu to find insights
5. Determine if patterns found indicate potential fraud or money laundering
    a. Describe how you've come to your conclusion
    b. Support with visualizations (Tableu)

## Installation
Clone this repository to your local machine
```
git clone https://github.com/akouirouk/financial_data_analysis.git
```
Make sure you have Python installed (first command for Windows machine, second command for Mac machine)
```
python --version
python3 --version
```
If you do not have Python installed, please [install](https://www.python.org/downloads/) the latest version of Python

## Usage
Create python virtual environment (first command for Windows machine, second command for Mac machine)
```
python -m venv venv
python3 -m venv venv
```
Activate Python virtual environment
```
source venv/bin/activate      
```
Install dependencies
```
pip install -r requirements.txt
```
Run script to generate cleaned dataset and visualizations
```
python main.py
```