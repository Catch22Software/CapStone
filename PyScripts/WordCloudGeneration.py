from wordcloud import WordCloud
import matplotlib.pyplot as plt
import copy
import csv

'''
Title: CapStone Project
Author: James Mills
Date: Jan 2022
This script was ran to create and save the WordCloud image used in the main notebook file.
'''
with open('../Data/transaction_data.csv', newline='') as f:
    read = csv.reader(f)
    holder = list(read)
master_list = []
for i in range(len(holder)):
    for j in range(len(holder[i])):
        master_list.append(copy.copy(holder[i][j]))  # flattens mult dim list to 1D for processing
print(len(master_list))  # length of total items -- 38765
cloud = WordCloud(width=16000, height=8000).generate(" ".join(master_list))
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
fig1 = plt.gcf()
plt.show()
fig1.savefig('../Images/wordcloud.png', dpi=400)  # creates and saves wordcloud image
