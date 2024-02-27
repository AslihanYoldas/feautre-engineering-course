import pandas as pd
## Load Datasets
def load_dataset(data_url='data/titanic.csv'):
    data =pd.read_csv(data_url)
    return data

def get_col_names(df, categoric_threshold = 10, cardinal_threshold = 20):
    """
    Gives the actual categorical, actual numerical and seems categorical but cardinal variable names
    Note: Categoric variables includes seems like numerical categorical variables

    Parameters
    -------
    df: dataframe- Dataframe to get variable names    
    categoric_threshold: int, optional - numeric but categorical variables threshold value
    cardinal_threshold: int, optional - categoric but cardinal variables threshold value
    Note: Thresholds can change according to dataset
    Returns
    -------
    categoric_cols:list -List of cat variables
    num_cols:list - List of numerical variables
    cat_but_car: list - List of cardinal variables


    """
    # Getting the all look like categorical variables
    categorical_cols = [col for col in df.columns if df[col].dtypes == "O"]
    # Getting the seems like numerical but categorical variables
    # If class number (unique value) lower than categorical threshold it is a categorical variable not numerical
    num_but_cat = [col for col in df.columns if df[col].nunique() < categoric_threshold and df[col].dtypes != "O"]
    # Getting the seems like categorical but cardinal variables
    # If class number (unique value) bigger than cardinal threshold it is a cardinal variable not categorical
    cat_but_car = [col for col in df.columns if df[col].nunique() > cardinal_threshold and df[col].dtypes == "O"]
    # Getting the actual categorical variables added the numerical categorical and substract cardinal categorical variables
    categorical_cols = categorical_cols + num_but_cat
    categorical_cols = [col for col in categorical_cols if col not in cat_but_car]
    
    # Getting the all look like numerical variables
    num_cols = [col for col in df.columns if df[col].dtypes != "O"]
    #Getting the actual numerical variables by substracting numeric categorical variables
    num_cols = [col for col in num_cols if col not in num_but_cat]
    
    print(f"Observations:{df.shape[0]}")
    print(f"Variables:{df.shape[1]}")
    print(f"categorical columns:{len(categorical_cols)}")
    print(f"numerical columns:{len(num_cols)}")
    print(f"cardinal columns:{len(cat_but_car)}")
    print(f"numeric but categorical variables:{len(num_but_cat)}")
    # num_but_cat is in categorical variables
    return categorical_cols, num_cols, cat_but_car

