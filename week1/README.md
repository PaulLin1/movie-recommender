# movie-recommender

You probably interact with a recommendation system every day. Whether it's the food suggestions on your maps app or the Tiktok algorithm that recommends what to watch next, an algorithm is controlling what content you see. The concept is simple, but slight inaccuracies can lead to less activity from users and even churn. Think about all the times you closed Tiktok or Instagram reels because the content you were getting just didn't fit your current mood. 

In this project we'll be creating a movie recommendation system. Similar to the other examples, having an accurate movie recommendation system can boost the amount of customers and the time they spend on your app. Imagine having Netflix, but not knowing what movies are available. You wouldn't use the app very much would you?

Before we build the recommendation system, we first have to define what is is. There can be various different types of recommendation systems within a single platform. For example, Netflix has recommendations when you open up the app, recommendations for what to watch next, and more. Each one is a different algorithm that is tailored for a certain purpose. In this project, we will be focusing on the first 2 examples, starting with the second one. As we progress, we will learn about more methods we can use to predict someone's taste.

Now that we know what we're building, lets breakdown some key concepts that we will need to understand before we start.

## Inputs

The inputs to a machine learning system are called features. This is what we'll use to predict what someone would want to watch next. This consists of what they have watched, rated highly in the past, or interacted with in any other way. The movies themselves also have feature too. This includes the year they were released, their genre, and even the ratings other users other people haven given them in the past (Hint: we'll be using this data in a future week).

## Outputs

This may seem self explanatory, but it really isn't. Yes, the output is movies, but how many? What information should you output? For the two types of recommendation system's you'll see that it is very different. In a ML system, the presentation is just as important as the outputs themselves.

## Data

Data is one of, if not the most important thing, for machine learning. This is because data is used to train a model, instead of explicitly defining it yourself. It is important to have both quantity AND quality. Quantity ensure you have enough data to generalize to unseen examples and quality ensures the predictions are accurate. For this project, you can choose whatever dataset of movies you want. However, for sake of simplicity and for teaching, we recommend starting with the ones we curated. Links to download them are here (https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) and here (https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data). We may introduce more in the future, but make sure you have these 2 downloaded.

## User Interface (UI)

Our project will solely be a movie recommendation system. However, we will try to mimic the types of recommendations streaming services do. Therefore, we created a simple UI (Flask app) that will serve as the front end of our system.  To participate in this project, you can leave the UI as it is, but if you like, you can customize it. Some ideas for customization is adding movie posters, more movie details, and more CSS styling.

# Setting up our environment

1. Clone the repository here
2. Create a python virtual environment
    python -m venv venv to create it
    source venv/bin/activate to go into it
3. Download the requirements into the virutal environment
    pip install -r requirements.txt
    Note: there will be more packages needed in the future, but these are the ones you need right now.
4. Run python app.py
    You should be able to see a flask app that aleady has search bar and a simple display for the movies
    Click around the site to see all of its features
5. Add your data
    Add the data you downloaded to the repository folder
    Add the data to your .gitignore file if it not already in there
        Pushing this data is not recommended because it takes a lot of time and is not getting modified.

Congratulations! You are all set to start this project. Right now you should have a functioning website that just displays movies. 
