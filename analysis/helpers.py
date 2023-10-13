from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def encode_and_bind(df: pd.DataFrame, feature: str) -> pd.DataFrame:
    """Encode columns with 'dummy' values and bind to original Pandas DataFrame.

    Args:
        df (pd.DataFrame): Containing raw transaction data
        feature (str): The column to encode

    Returns:
        pd.DataFrame: Newly created Pandas DataFrame with encoded columns
    """

    # create encoder object
    encoder = OneHotEncoder(sparse_output=False)
    # reshape column to 2D-array
    column = df[feature].values.reshape(-1, 1)
    # encoded columns
    encoded_columns = encoder.fit_transform(column)

    # reset df index
    df = df.reset_index(drop=True)
    # create new df with encoded columns
    encoded_df = pd.DataFrame(
        encoded_columns, columns=encoder.get_feature_names_out([feature])
    )

    # concat from encoded_df with df
    encoded_data = pd.concat([df, encoded_df], axis=1)
    # return the one-hot encoded dataframe
    return encoded_data
