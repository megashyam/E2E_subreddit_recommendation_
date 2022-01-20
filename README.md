# E2E_subreddit_recommendation_
This is an end to end subreddit recommendation project using python 



## _What is collaborative based filtering?_
Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users.

![lisa](https://github.com/megashyam/E2E_subreddit_recommendation_/blob/main/preproccesing/gif.mp4)

It works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user. It looks at the items they like and combines them to create a ranked list of suggestions.

![alt_text](https://github.com/megashyam/E2E_subreddit_recommendation_/blob/main/preproccesing/f35bf62d-recommendation-engine-1.png)

## The dataset:
The data set consists of 1.74 million comments for which the user, the name of the subreddit and the number of comments in this subreddit were saved. The dataset folder has two .csv files, the subreddit description and information and the user comment count.

## Similarity Score :
How does it decide which item is most similar to the item user likes? Here we use the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

