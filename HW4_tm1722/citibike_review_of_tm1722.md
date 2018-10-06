uak211 review of tm1722 citibike project

#### null and alternative hypotheses formulation:
idea: people who ride citibikes on longer trips tend to be young

* The null hypothesis is well presented in boths words and formula to the extent it is mathematically testable- relies on an average trip duration during a specific timeframe for two specific populations. It could improve in two ways: specify a significance level, say of \alpha = 0.05, and specify the rider population in a way that accounts for riders who were born in 1960, not just before and after 1960.
* The alternative hypothesis correctly states in words and formula that the average time of riders born after 1960 minus the average time of riders born before 1960 during the specified timeframe would be greater than zero.

#### data to support the project:
* For testing these hypotheses, we need to see data relating to trip duration, old/young age categorization, and the specified timeframe. Trip duration data is included and the data prep does account for people born on or before 1960, which addresses the above concern about specifying riders born in 1960. The data pull and prep ensure the data includes only the specified time frame.
* The included scatterplot is helpful in understanding the distribution of the sample trip durations.

#### possible modifications to test: creating additional age categories within the predictor variable, which would transform it from a categorical to ordinal variable.

#### appropriate test:
* This hypothesis is testing the mean trip duration of two specified sample populations, so we are dealing with a numeric outcome variable. We have a single predictor variable, which is ordinal (born before/on 1960 or born after).
* the alternative hypothesis states the mean trip duration for young riders is longer, so we are interested in a one-tailed test. 
* We don't know the parameters of the population, so the z-test or student's t-test, which at first may seem appropriate, are not usable here. For a categorical predictor variable, a chi-square test of equality of proportions would be suitable.

For nonparametric tests of sample means with ordinal predictor variables (if you add additional age categories), a Wilcoxon-Mann Whitney test is appropriate.

I often reference this [table](https://stats.idre.ucla.edu/other/mult-pkg/whatstat/) for choosing an appropriate test. 

