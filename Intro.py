import matplotlib.pyplot as plt

#data
languages = ['Python', 'Java', 'C', 'C++', 'JavaScript']
Usage = [60,70,75,65,85]

#bar plot
plt.bar(languages,Usage)

#labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Usage Percentage')
plt.title('Programming Language Popularity')

#show plot
plt.show()