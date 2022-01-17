import pandas as pd
import csv
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
'''
Title: CapStone Project
Author: James Mills
Date: Jan 2022
This script was ran to complete the rules association creation for the item set.
'''
with open('../Data/transaction_data.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    sample_data = list(reader)
te = TransactionEncoder()
te_ary = te.fit(sample_data).transform(sample_data)  # take transaction data and transform into df
df = pd.DataFrame(te_ary, columns=te.columns_)
print(len(df))  # length of initial hot-encoded pandas dataframe 3898
frequent_1 = apriori(df, min_support=0.0025654, use_colnames=True)  # support for at least 10 of the 3898 transactions
print(len(frequent_1))  # length of initial rules with 167 total unique items 34612
frequent_1.head()
rules_1 = association_rules(frequent_1, metric="confidence", min_threshold=0.5)
# adds a cutoff of at least 50% confidence
print(len(rules_1))  # length of resulting ruleset 24694
rules_1.consequents.unique()
print(len(rules_1.consequents.unique()))  # amount of unique consequent recommendations 47
rules_1.to_csv('../Data/master_rules.csv')
