# BayesianLearning
Bayesian learning for classifying news text articles using Naive Bayes classifiers.
1. The data is read from the first 500 files in all the category.
2. The stop words, numbers and special characters are removed from the data.
3. The data is split into list of words.
4. The data of 500 files in each category is used as training data and the rest is used as testing data.
5. The number of times the collected words are repeated is counted in all the files in every category used and the probability of each word is found.
6. The remaining 500 files are read, and the first three steps are repeated.
7. For each file, predict the category using the formula for p:
𝑝𝑟𝑒𝑑𝑖𝑐𝑡 𝑓𝑖𝑙𝑒 = 𝑎𝑟𝑔𝑚𝑎𝑥{𝑃 𝑌 ∗ 𝑃(𝑥4|𝑌).
8. If the predicted category = the actual category, then it is a correct assumption.
9. Accuracy is then calculated by using the formula : correct assumptions/total number of files used for testing.
