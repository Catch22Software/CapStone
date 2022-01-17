# BINDER LINK TO VOILA VERSION
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Catch22Software/CapStone/HEAD?urlpath=voila%2Frender%2FC964_Final_Product.ipynb)
# CapStone
- C964_Final_Product.ipynb is main notebook file.

# Data
- Data is located under Data folder. Unaltered dataset is contained in Groceries.dataset.csv.
- master_rules.csv contains the association rules.
- names.csv contains the 167 unique item names.
- transaction_data.csv is the dataset filtered to list each unique customer's grocery data as a list.

# PyScripts
- DataCleaning.py is the initial process of creating the transaction_data.csv file.
- RuleCreation.py is the initial process of creating the master_rules.csv file.
- WordCloudGeneration.py created the WordCloud image used in the main .ipynb file.
- HashTable.py is used to create a searchable Inventory using O(1) complexity.

# OTHER NOTEBOOKS

Files will be dropped once output data is utilized to add examples to supporting document.


### NOTE

Pandas handles writing a csv file that contains Python frozenset in a weird way.
It writes the cell data as a String and adds the `frozenset({})` container around
the cell data.

Due to this constraint, there is a line of code that only runs once per notebook
execution that correctly formats both the antecedent and consequent 
columns as`frozenset()`.

From this all of the queries to provide recommendations are done correctly using
frozenset to only use combinations instead of permutations.


## AUTHOR
- James Mills
## DATE
- January 2022

####Backup Binder URL

https://mybinder.org/v2/gh/Catch22Software/CapStone/HEAD?urlpath=voila%2Frender%2FC964_Final_Product.ipynb

##### DEDICATION
-I want to thank my beautiful fiancée, Vennessa, for ALWAYS being there for me. Even
through all of the long, gruelling nights or non-stop computer time to get my degree
finished. I could never have done this without her and her support!! Looking forward
to our next chapter over the horizon!!! I love you 
3.14159265 ♥♥♥
