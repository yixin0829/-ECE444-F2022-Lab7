# ECE444-F2022-Lab7
Deploy a fake news model with `Flask REST API`, `AWS Elastic Beanstalk` and additionally created CICD pipeline using `AWS CodePipeline`. Every push to this repo's main branch will trigger a CD.

## Part 2: API Latency Test
The testing function and four test cases are included in [api_latency_testing.py](./tests/api_latency_testing.py). Below are the testing results:

| Test Case | Test Input                                    | Expected Response | Actual Response | Average Latency Over 100 Calls (ms) |
| --------- | --------------------------------------------- | ----------------- | --------------- | ----------------------------------- |
| 1         | "Donald Trump was an U.S. president."         | 0                 | 0               | 152.3                               |
| 2         | "The Wall Street Journal is founded in 1889." | 0                 | 1               | 152.1                               |
| 3         | "Donald Trump Achieves World Peace!"          | 1                 | 1               | 151.6                               |
| 4         | "Elon Musk bought Google with 1$"             | 1                 | 1               | 151.8                               |

## Appendix
- Beanstalk's running environment
![image](https://user-images.githubusercontent.com/56566212/204156207-3a16a101-bf34-4436-ad97-087c0bac3c4c.png)
- CICD setup using CodePipeline
![image](https://user-images.githubusercontent.com/56566212/204156259-8c2d38c1-b1a0-4eb3-ae8a-ef333e731238.png)
- http://lab7.eba-ficycrcw.us-east-2.elasticbeanstalk.com/predict?text=hello
![image](https://user-images.githubusercontent.com/56566212/204154841-66194562-c55b-4c5c-abd4-0dd5beeba55d.png)
- http://lab7.eba-ficycrcw.us-east-2.elasticbeanstalk.com/
![image](https://user-images.githubusercontent.com/56566212/204155270-68079983-d26f-4d1a-b151-f6a045e01e20.png)

