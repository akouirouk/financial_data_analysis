import pandas as pd

from data_prep.clean import clean_df, dataframe_insights
from analysis.filter_data import create_pivot_table
from data_prep.validate import validate_df
from analysis.filter_data import (
    get_transactions_over_amount,
    transactional_data_per_hour,
)
from load_data.to_mysql_table import load_csv_into_mysql
from analysis.fraud_detection import (
    consecutive_fraudulent_hours,
    zero_amount_transactions,
    fraud_detection,
)

if __name__ == "__main__":
    # read original CSV file into data
    raw_df = pd.read_csv("./data/input/paysim_data.csv")
    # get some general info on the raw data
    dataframe_insights(raw_df)

    # clean the data
    clean_df("./data/input/paysim_data.csv")
    # validate the cleaned data
    cleaned_df = validate_df("./data/output/cleaned_paysim_data.csv")
    # insert cleaned df into mysql table
    load_csv_into_mysql()

    # write filtered dataframe to CSV file
    get_transactions_over_amount(cleaned_df, "amount", 200000.00)

    # get number of transactions where the amount == 0
    zero_amount_transactions = zero_amount_transactions(cleaned_df)

    # create pivot table from cleaned_df
    pivot_table = create_pivot_table(cleaned_df)

    # get number transactional volume per hour
    transactions_by_hour = transactional_data_per_hour(cleaned_df, 1, 743)
    # hours that consist of 100% fraudulent transactions
    df_fraudulent_hours = transactions_by_hour[
        transactions_by_hour["percentage_of_fradulent_transactions"] == 100
    ]
    # convert "hour" column to list
    fraudulent_hours = df_fraudulent_hours["hour"].to_list()
    # get the number of instances of consecutive fraud and average number of consecutive fraudulent hours
    consecutive_fraudulent_hours(fraudulent_hours)

    # create dataframe of transactions in fraudulent hours
    transactions_in_fraudulent_hours = cleaned_df[
        cleaned_df["hour"].isin(fraudulent_hours)
    ]

    # get the precision score from the random forest
    avg_precision_score = fraud_detection(cleaned_df)
    print(
        f"The average precision score of the current fraud detection system is: {avg_precision_score}%"
    )
