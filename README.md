# Graphical Representation of Irrational States (GRIS)

## Overview
GRIS is a research project for my undergraduate honor's thesis at the School of Behavioral and Brain Sciences at the University of Texas of Dallas. The goals of this project is to:

1. Create concept graphs from Reddit posts of people with psychotic disorders and people without psychotic disorders
2. Use a graph neural network to differentiate between the concept graphs of these two populations
3. Extract meaningful information from the neural networks to learn about the differences between these two populations
4. Determine if there are any differences in the concept graphs of these two populations

## Steps

### Data Wrangling
To get textual data from people with schizophrenia, I used the PushShift API to query posts from the subreddit r/schizophrenia. I then got a list of authors and their user flair based on the posts from the subreddit. To ensure I was only using authors that had schizophrenia, I checked if their user flair indicated they had a diagnosis of schizophrenia spectrum disorder and kept the authors that had those user flairs. After that, I queried a list of posts written by each psychotic author that span multiple subreddits. My reasoning for this is to ensure the textual data is diverse in content instead of only focusing on the topic of psychosiss. I then filtered out posts that were less than 50 tokens long and put the posts in a list matched to each author in a mapping.

To get textual data from a non-psychotic population, I queried all Reddit posts within a timeline using the PushShift API. I then got a list of authors who written those posts and excluded those authors that were already in the schizophrenia population. After that, I got a list of posts that were more than 50 tokens long made by each author and mapped them to the username of the author.

## Data Format

### data/author.pickle
A Python dictionary where the key is the psychotic author's username and the value is the author's user flair.

### data/psychotic_posts.pickle
A Python dictionary where the key is the psychotic author's username and the value is a list of dictionaries with the key/value pairs being the subreddit of a post, the textual content of the post, and the length of the post.

### data/random_authors.pickle
A Python list of non-psychotic authors' usernames.

### data/nonpsychotic_posts.pickle
A Python dictionary where the key is the non-psychotic author's username and the value is a list of dictionaries with the key/value pairs being the subreddit of a post, the textual content of the post, and the length of the post.
