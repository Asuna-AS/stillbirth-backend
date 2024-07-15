<h1 align="center">Risk Analysis and Calculator for Stillbirth</h1>
<h2 align="center">This Repository contains the backend files and model for the Risk analysis and stillbirth calculator app !!</h2>

### Installation

Setup Application on local machine: 

1. Clone the repo
   ```sh
   git clone https://github.com/Asuna-AS/stillbirth-backend.git
   ```
2. Install required libraries from requirements.txt file
   ```sh
   pip install -r requirements.txt
   ```
3. Start the server
   ```sh
   flask --app app.py run
   ```
## Workflow

The project follows a specific workflow:

![soft-workflow-stillbirth](https://github.com/Asuna-AS/stillBirthPredictionApp/assets/75484060/8c20d145-dc7a-463f-bc7b-69eba1b23d78)

## Machine Learning Model Workflow

Our ML workflow consists of data input, Explanable AI analysis, risk prediction, and data integration:

![ml-workflow-stillbirth](https://github.com/Asuna-AS/stillBirthPredictionApp/assets/75484060/1531213a-2272-49e5-84e2-e9a893a3cbf8)

## Results and Discussion

We applied several ML algorithms and identified logistic regression and random forest as the models with the best accuracy and precision for predicting stillbirth risk. The final prediction categorizes the likelihood of stillbirth into three levels:

1. Low chances (less than 30%)
2. Mediocre chances (between 30% and 60%)
3. High chances (greater than 60%)
   
## Authors
- Arunim Singhal (Btech @ Indian Institute of Information Technology Lucknow)
- Priya Sharma (Btech @ Indian Institute of Information Technology Lucknow)


## Mentor
- Dr. Mainak Adhikari (Head of Department - Computer Science) @ Indian Institute of Information Technology Lucknow
