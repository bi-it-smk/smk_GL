import pandas as pd

def att_avg(df):
    data = df[
        (df["workday"]==1)
    ]
    return data["present"].mean()

def year_avg(df):
    cur_year = pd.Timestamp.today().year
    data = df[
        (df["date"].dt.year == cur_year) &
        (df["workday"] == 1)
    ]
    return data["present"].mean()

def month_avg(df):
    today = pd.Timestamp.today()
    data = df[
        (df["date"].dt.year == today.year) &
        (df["date"].dt.month == today.month) &
        (df["workday"] == 1)
    ]
    return data["present"].mean()

def monthly_averages(df):
    data = df[
        (df["workday"] == 1)
    ]
    return(
        data.groupby(
            data["date"].dt.to_period("M")
        )["present"].mean()
    )

