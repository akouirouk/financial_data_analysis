import pandas as pd


def get_transactions_over_amount(
    df: pd.DataFrame, column: str, amount: float
) -> pd.DataFrame:
    """Return a Pandas DataFrame of all transactions over a certain amount.

    Args:
        df (pd.DataFrame): The DataFrame containing the raw data
        column (str): The target column in the DataFrame
        amount (float): The maximum amount in a single transfer

    Returns:
        pd.DataFrame: The filtered DataFrame
    """

    # filter dataframe if column value is over amount
    filtered_df = df[df[column] >= amount]
    # save filtered_df to file
    filtered_df.to_csv("./data/output/over_200k.csv", index=False)

    return filtered_df
