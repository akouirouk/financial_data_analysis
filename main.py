from data_prep.validate import validate_df
from data_prep.clean import clean_df


if __name__ == "__main__":
    # clean the data
    clean_df("./data/input/paysim_data.csv")
    # validate the cleaned data
    validate_df("./data/output/cleaned_paysim_data.csv")
