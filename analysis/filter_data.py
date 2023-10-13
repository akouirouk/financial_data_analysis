import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def transactional_data_per_hour(
    df: pd.DataFrame, start_hour: int, end_hour: int
) -> pd.DataFrame:
    """Average the amount of money that is transacted per hour

    Args:
        df (pd.DataFrame): Contains the transaction data
        start_hour (int): The first hour to account for
        end_hour (int): The last hour to account for

    Returns:
        pd.DataFrame: The hourly transactional volumne
    """

    # assert that the start and end hours are within the range provided in the dataset
    assert start_hour >= 1 and start_hour <= end_hour
    assert end_hour <= 743

    # initialize dict
    consolidated_data = {}

    # loop through each hour in a 24 hour day
    for hour in range(start_hour, end_hour + 1):
        # get all transactions from that hour in a df
        hour_df = df[df["hour"] == hour]
        # get the sum of the "amount" column
        volume = round(sum(hour_df["amount"].to_list()), 2)

        # most frequent transaction type
        most_frequent_type = hour_df["type"].value_counts().idxmax()
        # occurances of the most frequent transaction type
        df_most_frequent_type = hour_df[hour_df["type"] == most_frequent_type]
        # number of most frequent type transactions
        most_frequent_type_occurances = df_most_frequent_type.shape[0]
        #
        most_frequent_type_volume = round(
            sum(df_most_frequent_type["amount"].to_list()), 2
        )

        # get the number of transactions by indexing the number of rows from hour_df.shape
        number_of_transactions = hour_df.shape[0]
        # calculate the percentage of fradulent transactions
        number_of_fradulent_transactions = hour_df[hour_df["is_fraud"] == 1].shape[0]
        # percentage of fraudulent transactions from total number of transactions per hour
        percentage_of_fraudulent_transactions = round(
            ((number_of_fradulent_transactions / number_of_transactions) * 100), 2
        )

        # construct dict
        data = {
            "hour": hour,
            "volume": volume,
            "number_of_transactions": number_of_transactions,
            "percentage_of_fradulent_transactions": percentage_of_fraudulent_transactions,
            "most_frequent_type": most_frequent_type,
            "most_frequent_type_volume": most_frequent_type_volume,
            "number_of_most_frequent_type_transactions": most_frequent_type_occurances,
        }
        # update consolidated_data with data
        consolidated_data[hour] = data

    # convert json object to dataframe and transpose the df
    transactional_data_df = pd.DataFrame(consolidated_data).T
    # convert dataframe to CSV file
    transactional_data_df.to_csv(
        "./data/output/transactional_data_per_hour.csv", index=False
    )

    # return the transactional data
    return transactional_data_df


def get_transactions_over_amount(
    df: pd.DataFrame, column: str, amount: float
) -> pd.DataFrame:
    """Return a Pandas DataFrame of all transactions over a certain amount.

    Args:
        df (pd.DataFrame): Contains the raw data
        column (str): The target column in the DataFrame
        amount (float): The maximum amount in a single transfer

    Returns:
        pd.DataFrame: The filtered DataFrame
    """

    # filter df if column value is over amount
    filtered_df = df[df[column] >= amount]
    # save filtered_df to file
    filtered_df.to_csv(f"./data/output/transactions_over_{amount}.csv", index=False)

    return filtered_df


def create_pivot_table(df: pd.DataFrame) -> pd.pivot_table:
    # create the pivot table from df
    pivot_table = df.pivot_table(
        index=["type"],
        values=["amount", "is_fraud"],
        aggfunc=["sum", "std"],
        margins=True,
    )

    # set color palette for pivot table
    cm = sns.light_palette("purple", as_cmap=True)
    # set the color gradient
    pivot_table.style.background_gradient(cmap=cm)

    # convert pivot table to CSV and save to file
    pivot_table.to_csv("./data/output/pivot_table.csv", index="type")

    # return the pivot table
    return pivot_table
