from pandera.typing import DataFrame, Series
import pandera as pa
import pandas as pd

from pathlib import Path


class PaySimSchema(pa.SchemaModel):
    """Schema for PaySim dataset."""

    hour: Series[int] = pa.Field(nullable=False, ge=1)
    type: Series[str] = pa.Field(nullable=False)
    amount: Series[float] = pa.Field(nullable=False, ge=0.0)
    initiator_id: Series[str] = pa.Field(nullable=False)
    initiator_old_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    initiator_new_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    target_id: Series[str] = pa.Field(nullable=False)
    target_old_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    target_new_balance: Series[float] = pa.Field(nullable=False, ge=0.0)
    is_fraud: Series[int] = pa.Field(nullable=False, ge=0, le=1)


@pa.check_types(lazy=True)
def validate_df(path: Path) -> DataFrame[PaySimSchema]:
    """Validates the data in a Pandas DataFrame

    Args:
        path (Path): The file path to the Pandas DataFrame
    """

    # return read CSV file into dataframe
    return pd.read_csv(path, encoding="utf-8")
