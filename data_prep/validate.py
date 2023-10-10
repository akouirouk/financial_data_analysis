from pandera.typing import DataFrame, Series
import pandera as pa
import pandas as pd

from pathlib import Path


class PaySimSchema(pa.SchemaModel):
    """Schema for PaySim dataset."""

    hour: Series[int] = pa.Field(nullable=False, ge=1)
    type: Series[str] = pa.Field(nullable=False)
    amount: Series[float] = pa.Field(nullable=False, ge=0.0)
    sender: Series[str] = pa.Field(nullable=False)
    sender_old_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    sender_new_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    recipient: Series[str] = pa.Field(nullable=False)
    recipient_old_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    recipient_new_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    is_fraud: Series[int] = pa.Field(nullable=False, ge=0, le=1)
    exceeds_transaction_limit: Series[int] = pa.Field(nullable=False, ge=0, le=1)


@pa.check_types(lazy=True)
def validate_df(path: Path) -> DataFrame[PaySimSchema]:
    """Validates the data in a Pandas DataFrame

    Args:
        path (Path): The file path to the Pandas DataFrame
    """

    # return read CSV file into dataframe
    return pd.read_csv(path, encoding="utf-8")
