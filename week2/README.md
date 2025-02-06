# Week2

Welcome to Week 2 of the AI Club movie recommender project. Last week, we formalized what we are building and setup our environment. This week, we will be looking at the data we downloaded last week and transforming it so it for our ML models in the following weeks.

# Data

Data is the single most important thing for ML. Last week, we downloaded a dataset of movies with their features. However, for a real ML project, the process of gathering data takes much longer because you are often the ones collecting, we merely collected it from other sources. Now that we have it downloaded, take a look at it. The data is pretty readable for humans. You'll see that it has a basic information about movies, like the year, release date, etc. Intuitively, you can see how this data would be useful for movie recommendation. If someone likes movies from the 60's, it would be a fair prediction to recommend them a movie from that era. But what about data like plot summary? How can you compare 2 paragraph long plot summaries. Think about this by yourself. Would you compare each word and count how many they have in common? Maybe just look at proper nouns? This would be pretty time consuming, even for a computer. Keep these questions in mind while we go and try to transform each feature we have.

# Setup

For data exploration, it is common to use Jupyter Notebooks. If you already have experience with Jupyter Notebooks, you can skip this section. However, if you do not, watch this video: .

Now, create a folder called notebooks in you repo. It is good practice to keep them in a seperate folder. For simplicity, we have provided a Jupyter Notebook you can use here. 

# The intuitive features

Like described earlier, some features are pretty intuitive. Years are simple because they already numbers and have a simple sense of closeness. If 2 years are the same, there must exist some correlation between the two movies. Even if they are similar, but not the same, like 1999 and 2000, its obvious that they are similar. For features like these, which also includes rating and popularity, we can leave them be for the most part. But what about them do we need to change? We need to normalize them. Please read this article for an extensive introduction to the topic   . This is useful because say if a movie and its remake are from 1960 and 2022, they would be super far apart. However, pretty much every feature should be the same, including the description, genre, etc. And someone who liked the original may also want to watch the remake. However, since years have such a big range, the gap may outweigh all the other features. Errors like this causes biases that we do not intend. Yes, having some bias may be useful, like obviously two movies having the same name should outweight some features, but to start with, it is a good idea ot normalize all the features to begin with.

