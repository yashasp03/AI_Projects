## Topic Modelling Using Latent Dirichlet Allocation (LDA)

Topic modelling aims to uncover hidden thematic structures within a collection of documents. This project utilizes Latent Dirichlet Allocation (LDA), a widely-used model in natural language processing, to identify topics within a large text corpus.


## Key Points

Model Used: LDA characterizes each topic by a distribution over words and maximizes the posterior probability of the entire corpus given the topics and words.

Training Phase: The model is trained on two topics:
Topic 0: Related to artificial intelligence.

Topic 1: Related to football.

Testing Phase: Evaluates a new document to determine its association with the predefined topics.
Discussion

Topic Characteristics: During training, the model identifies words associated with each topic:
Topic 0 (Artificial Intelligence): Words such as human, intellig, machin, field, associ.

Topic 1 (Football): Words such as play, team, goal, game, ball.

Word Matching Percentage: After testing a new document, the output indicates:
Artificial Intelligence Topic: 50.67% of words match the words associated with artificial intelligence.

Football Topic: 49.32% of words match the words associated with football.


## Features

LDA Implementation: Implements Latent Dirichlet Allocation for topic modelling.

Topic Interpretation: Identifies and characterizes topics based on word distributions.

Model Training: Trains the LDA model on a corpus to uncover latent topics.

Topic Evaluation: Evaluates new documents to determine their relevance to predefined topics.

Word Matching Analysis: Provides detailed percentages of word matches for each identified topic.