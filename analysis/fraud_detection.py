from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

from analysis.helpers import encode_and_bind


def fraud_detection(df: pd.DataFrame) -> float:
    """Detect if there is a pattern of fraud by using the Random Forest (RF) Alogorithm.

    Args:
        df (pd.DataFrame): The cleaned transaction data

    Returns:
        float: The precision score from the RF
    """

    # drop columns that will not be used in the model
    df.drop(["initiator_id", "target_id"], axis=1, inplace=True)
    # tokenize the "type" column to not be included in the model
    encoded_df = encode_and_bind(df, "type")

    # create trains
    X = encoded_df.drop(["is_fraud", "type"], axis=1)
    y = encoded_df[["is_fraud"]]
    # train and test model
    train_X, test_X, train_y, test_y = train_test_split(
        X, y, test_size=0.2, random_state=121
    )

    # create RF object
    clf = RandomForestClassifier(n_estimators=15)
    # make predictions
    probabilities = clf.fit(train_X, train_y.values.ravel()).predict(test_X)

    # return the average precision score from the model
    avg_precision_score = round(
        (average_precision_score(test_y, probabilities) * 100), 2
    )
    return avg_precision_score


def consecutive_fraudulent_hours(numbers: list) -> None:
    """Determine the number of instances consecutive hours comprised of only fraudulent transactions.

    Args:
        numbers (list): Hours from when transactions occured
    """

    try:
        # index the first elememt in numbers
        numbers[0]
    except IndexError:
        # raise IndexError if the list is
        raise IndexError(f"The list parameter supplied does not contain any elements.")

    # initialize list to store consecutive_numbers
    fraudulent_hours = []
    # index the first number in list and set it to train ("train" of chronological numbers)
    train = [numbers[0]]

    # loop through the length of numbers
    for i in range(1, len(numbers)):
        # if the next number in the list equals the previous number
        if numbers[i] == numbers[i - 1] + 1:
            # append next number to current_group
            train.append(numbers[i])
        # if the next number is not the next chronological number
        else:
            # create a new group (list) in gropued
            fraudulent_hours.append(train)
            # set first number in list to current number
            train = [numbers[i]]

    # append the current group to grouped
    fraudulent_hours.append(train)

    # keep list of consecutive numbers is len() is >= 2
    validated_consec_hours = [
        consec_hours for consec_hours in fraudulent_hours if len(consec_hours) >= 2
    ]

    # initialize list to store averages of length for each group of consecutive numbers
    avg_consect_hours = []
    # loop through consecutive groups
    for numbers in validated_consec_hours:
        # append length of grouped list to avg_consect_nums
        avg_consect_hours.append(len(numbers))

    # print to log
    print(f"Instances of Consecutive Fraudulent Hours: {len(validated_consec_hours)}")
    print(
        f"Average number of Consecutive Fraudulent Hours: {round(sum(avg_consect_hours) / len(avg_consect_hours), 2)}"
    )


def zero_amount_transactions(df: pd.DataFrame) -> int:
    """Gets the number of transactions where the amount is 0.

    Args:
        df (pd.DataFrame): Contains the transaction data

    Returns:
        int: The number of transactions where the amount is 0.
    """

    # df subset where the amount is 0
    transactions = df[df["amount"] == 0]
    # convert transactions to CSV file
    transactions.to_csv("./data/output/transactions_with_0_amount.csv", index=False)
    # index the shape (rows) of the df
    return transactions.shape[0]


def check_balances(df: pd.DataFrame) -> pd.DataFrame:
    """Return a Pandas DataFrame of transactions where the balance does not properly adjust for amount transacted.

    Args:
        df (pd.DataFrame): Contains the transaction data

    Returns:
        pd.DataFrame: The non-mathematically sound transactions
    """

    # extract the "type" of the transaction

    # run formulas based on the transaction type
    excpected_balance_diff = df["sender_old_balance"] - df["sender_new_balance"]
    # df["initiator_transaction_diff"] = [
    #    1 if expected_balance_diff == df["amount"] else 0
    # ]
