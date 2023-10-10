import pandas as pd
import numpy as np

from pathlib import Path


def clean_df(path: Path) -> None:
    """Clean the PaySim dataset and write to file

    Args:
        path (Path): The path of the CSV file containing the PaySim data

    Returns:
        pd.DataFrame: A cleaned DataFrame with the PaySim data
    """

    # set all floats to 2 decimal places
    pd.options.display.float_format = "{:.2f}".format

    # read CSV into dataframe
    df = pd.read_csv(path, encoding="utf-8")
    # drop duplicate rows
    df = df.drop_duplicates(keep="first")

    # define new column names
    renamed_columns = {
        "step": "hour",
        "nameOrig": "sender",
        "oldbalanceOrg": "sender_old_balance",
        "newbalanceOrig": "sender_new_balance",
        "nameDest": "recipient",
        "oldbalanceDest": "recipient_old_balance",
        "newbalanceDest": "recipient_new_balance",
        "isFraud": "is_fraud",
    }
    # rename columns
    df.rename(columns=renamed_columns, inplace=True)

    # select all columns of the object data type
    object_cols = df.select_dtypes(object).columns
    # strip all whitespace from values in object_cols
    df[object_cols] = df[object_cols].apply(lambda x: x.str.strip())

    # drop "isFlaggedFraud" column
    df = df.drop("isFlaggedFraud", axis=1)
    # create new column "exceeds_transaction_limit" and set to 1 if amount > 200000 else 0
    df["exceeds_transaction_limit"] = np.where(df["amount"] > 200000, 1, 0).astype(int)

    # columns that represent dollar amounts
    money_columns = [
        "amount",
        "sender_old_balance",
        "sender_new_balance",
        "recipient_old_balance",
        "recipient_new_balance",
    ]
    # loop through money_columns
    for column in money_columns:
        # remove non-numerical characters (except "." to distinguish cents)
        df[column] = df[column].astype(str).str.extract("(\d.+)", expand=False)
        # convert column to float
        df[column] = df[column].astype(float)

    # set the order of columns
    column_order = [
        "hour",
        "type",
        "amount",
        "sender",
        "sender_old_balance",
        "sender_new_balance",
        "recipient",
        "recipient_old_balance",
        "recipient_new_balance",
        "is_fraud",
        "exceeds_transaction_limit",
    ]
    # reorder columns
    df = df[column_order]

    # write cleaned dataframe to CSV
    df.to_excel("./data/output/cleaned_paysim_data.csv", index=False, encoding="utf-8")
