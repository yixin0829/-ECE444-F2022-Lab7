# ECE444-F2022-Lab7
Deploy a fake news model with Flask REST API, AWS Elastic Beanstalk and additionally created CICD pipeline using AWS CodePipeline. Every push to this repo's main branch will trigger a CD.

Examples:
- http://lab7.eba-ficycrcw.us-east-2.elasticbeanstalk.com/predict?text=hello
- http://lab7.eba-ficycrcw.us-east-2.elasticbeanstalk.com/

## Part 2: API Latency Test
The testing function and four test cases are included in [api_latency_testing.py](./tests/api_latency_testing.py). Below are the testing results:

| Test Case | Test Input                                    | Expected Response | Actual Response | Average Latency Over 100 Calls (ms) |
| --------- | --------------------------------------------- | ----------------- | --------------- | ----------------------------------- |
| 1         | "Donald Trump was an U.S. president."         | 0                 | 0               | 152.3                               |
| 2         | "The Wall Street Journal is founded in 1889." | 0                 | 1               | 152.1                               |
| 3         | "Donald Trump Achieves World Peace!"          | 1                 | 1               | 151.6                               |
| 4         | "Elon Musk bought Google with 1$"             | 1                 | 1               | 151.8                               |