import pandas as pd

def resample_multilabel_dataset(df, y_index, samples=200):
    
    # TODO: Catch dataframes that do not have y binary vectors
    
    """ Creates equal samples for multi-label classification which is useful when dealing
        with class imbalanced datasets.
        
    Args:
        df (dataframe): The imbalanced dataframe
        y_index (int): The position where the binary vectors y start (the features/columns being predicted)
        samples (int, optional): The number of samples for each label. Defaults to 200.

    Returns:
        Dataframe: A dataframe attempting to return an equal amount
    """
    df_resampled = []

    for i in df.iloc[:,y_index:].columns:
        new_df = df[df[i]==1]
        print(new_df.shape)
        df_resampled.append(new_df.sample(200, replace=True))
    
    # Concating the samples from each category into one and returning it.
    df = pd.concat(df_resampled)
    return df
