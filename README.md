# E2E_subreddit_recommendation_
This is an end to end subreddit recommendation project using python 
![](https://github.com/megashyam/E2E_subreddit_recommendation_/blob/main/preproccesing/videogify.gif)



## _What is collaborative based filtering?_
Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users.
It works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user. It looks at the items they like and combines them to create a ranked list of suggestions.

![alt_text](https://github.com/megashyam/E2E_subreddit_recommendation_/blob/main/preproccesing/f35bf62d-recommendation-engine-1.png)

## The dataset:
The data set consists of 1.74 million comments for which the user, the name of the subreddit and the number of comments in this subreddit were saved. The dataset folder has two .csv files, the subreddit description and information and the user comment count.

## Similarity Score :
How does it decide which item is most similar to the item user likes? Here we use the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## K-Nearest Neigbors:

 KNN is a non-parametric, lazy learning method. It uses a database in which the data points are separated into several clusters to make inference for new samples.
KNN does not make any assumptions on the underlying data distribution but it relies on item feature similarity. When KNN makes inference about a movie, KNN will calculate the distance between the target sub and every other movie in its database, then it ranks its distances and returns the top K nearest neighbor movies as the most similar sub recommendations.

![alt_text](https://miro.medium.com/max/1300/1*OyYyr9qY-w8RkaRh2TKo0w.png)


## Cosine Similarity
Cosine Similarity measures the cosine of the angle between two non-zero vectors of an inner product space. This similarity measurement is particularly concerned with orientation, rather than magnitude. In short, two cosine vectors that are aligned in the same orientation will have a similarity measurement of 1, whereas two vectors aligned perpendicularly will have a similarity of 0.

![alt_text](https://www.tyrrell4innovation.ca/wp-content/uploads/2021/06/rsz_jenny_du_miword.png)

