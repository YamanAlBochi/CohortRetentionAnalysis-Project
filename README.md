# CohortRetentionAnalysis-Project

- Retention Churn Rate is defined as the number of customers who continue to use a product/services, its measured as the number of returning users, at a regular interval such as every week or month, grouped by their week of signup, in this project I'll be exploring an online retail dataset and create a retention cohort analysis in Python..................

- What is Cohort Analysis?

A type of Statistical Analysis in which groups or 'Cohorts' of users are tracked through time to observe specific outcomes, the best way to think about cohort analysis, is that it's a form of experimentation to perform a Cohort Analysis, a company must first describe a hypothesis to test such a hypothesis that might be a new feature that will reduce churn rate. For example; a company will construct an experiment to monitor and such hypothesis over time, and as part of this experiment and design a company will have to define its user groups or cohorts for the experimentation to run, they do this by defining a unique characteristic that will define their cohorts. 

The data a user signing up online or creating an account, would be a good exapmle of this, a company will run the experiment based on the groups that they've defined, and they'll work out when they churn over time. finally once the company collected the data that they need, it displays in a format similar to this chart we have below in our Python File.


First, the rows display the customer cohorts from each time interval, what this describes is pretty simple any user that signs up to the app on January 1st fits into the first cohort, also any user that signs up on january 6 fits into the next cohort and so on and so forth.

In each column represents the amount of time that has elapsed since the user subscribed. so what this chart is describing as we move across it is the number of days since the user has subscribed, this means that day zero for the january 1 cohort is january 1 and day one is january the 2nd, if you take the January 2nd cohort, day zero is January 2nd and day one is January 3rd and ect..

Ever cell has an percentage, and what is this percentage means will be context dependent to the experiment and the hypothesis being tested, in our example; the percentage represents the number of active users still using the product within the cohort.. 

now, what a company could do with this information is where the true magic happens....

In our example, tracking across the chart gives us insight into when the users are churning and in wat proportion, as we can see in our chart, is describing a huge drop between day 0 and day indicating a large amounts of churn and as we run run down the chart we also see this dop-off is consistent across all users cohorts implying something big is causing users to churn within the first 24 hours of using any specific product, knowing this information means this company now has a starting point to daignose the potential problem allowing to be more precise in how to allocate resources to improve the problemm now while getting into the weeds of companies can further leverage this analytics technique.


The important takeaway, this technique is the foundation for data-driven product, marketing and customer success improvement efforts. Cohort Analysis isn't simply the domain of software as a service or digital companies either; a gym for example will have an attrition rate for both active use and churned membership, thus tere are numerous use cases for a gym to apply cohort analysis to and it should be an integral part of the marketing and product development processes, in summary; cohort analysis takes the guesswork out of where a company should be focusing its efforts to improve and all companies can benefit from cohort analysis when applied to their specific needs, they are the simple yet powerful tool that puts real data into the hands of the company so they can improve efficiently.


- Written by Yaman Al Bochi
