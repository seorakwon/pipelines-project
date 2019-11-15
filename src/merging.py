import cleaning
import scraping

def groupingData(df_row):
    '''
    Groups the data from the dataset with the data scrapped from the website
    '''
    group = pd.concat([data], [accident])
    group.to_csv('output/pipe.csv')

def get_operator():
    operator = group.loc[:, ["Operator","Year"]].groupby(['Operator']).count()
    operator = operator.sort_values(by="Year", ascending=False).head(10)
    return operator


def get_year():
    year = group.loc[:, ["Operator","Year"]].groupby(['Year']).count()
    year = year.sort_values(by="Operator", ascending=False).head(10)
    return operator
