# Heart Disease Prediction using Machine Learning

## Overview
The **Heart Disease Prediction** project is a machine learning-based system designed to predict the likelihood of heart disease based on patient data such as age, cholesterol levels, blood pressure, and other health indicators. By analyzing medical records and historical patient data, the model can provide an early warning system for heart disease risk.

This project is useful for doctors, healthcare professionals, and individuals to assess heart disease risks and take preventive measures accordingly.

## Features
- **Accurate disease prediction** using advanced machine learning algorithms
- **Data preprocessing and feature selection** for optimal model performance
- **Multiple machine learning models** compared to find the best approach
- **Web-based user interface** (optional) for easy access to predictions
- **Integration with medical datasets** for real-world application
- **Scalability** for future enhancements and additional features

## Technologies Used
- **Programming Language**: Python
- **Machine Learning Algorithms**: Logistic Regression, Random Forest, Decision Trees, XGBoost, Neural Networks
- **Data Handling & Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Deployment**: Flask (for API), Streamlit (for UI)
- **Database**: SQLite or PostgreSQL (optional for storing patient data)
- **Medical Dataset**: Public datasets like UCI Heart Disease dataset

## Column Description
- **age**: The person’s age in years
- **sex**: The person’s sex (1 = female, 0 = male)
- **cp**: chest pain type
        — Value 0: asymptomatic
        — Value 1: atypical angina
        — Value 2: non-anginal pain
        — Value 3: typical angina
- **trestbps**: The person’s resting blood pressure (mm Hg on admission to the hospital)
- **chol**: The person’s cholesterol measurement in mg/dl
- **fbs**: The person’s fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
- **restecg**: resting electrocardiographic results
        — Value 0: showing probable or definite left
- **restecg**: resting electrocardiographic results
        — Value 0: showing probable or definite left ventricular hypertrophy by Estes’ criteria
        — Value 1: normal
        — Value 2: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
- **thalach**: The person’s maximum heart rate achieved
- **exang**: Exercise induced angina (1 = yes; 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest (‘ST’ relates to positions on the ECG plot. See more here)
- **slope**: the slope of the
- **slope**: the slope of the peak exercise ST segment — 0: downsloping; 1: flat; 2: upsloping
- **ca**: The number of major vessels (0–3)
- **thal**: A blood disorder called thalassemia Value 0: NULL (dropped from the dataset previously)
        -Value 1: fixed defect (no blood flow in some part of the heart)
        -Value 2: normal blood flow
        -Value 3: reversible defect (a blood flow is observed but it is not normal)
- **target**: Heart disease (1 = no, 0= yes)

## Dataset
The dataset used for training includes multiple patient attributes such as:
- **Age**
- **Sex**
- **Chest pain type**
- **Resting blood pressure**
- **Cholesterol levels**
- **Fasting blood sugar**
- **Resting electrocardiographic results**
- **Maximum heart rate achieved**
- **Exercise-induced angina**
- **Oldpeak (ST depression induced by exercise)**
- **Slope of peak exercise ST segment**
- **Number of major vessels (0-3) colored by fluoroscopy**
- **Thalassemia type**

## Data Preprocessing
Before training the model, the dataset undergoes several preprocessing steps:
1. **Handling missing values** - Filling or removing incomplete records
2. **Encoding categorical variables** - Converting text data into numerical representations
3. **Feature scaling** - Normalizing numerical features for better model performance
4. **Outlier detection and removal** - Eliminating extreme values that can distort predictions
5. **Data splitting** - Dividing data into training and testing sets (typically 80-20 or 70-30 split)

## Model Selection
Multiple machine learning models are evaluated to find the best-performing one. The models include:
- **Logistic Regression** - A simple and interpretable classification model
- **Random Forest Classifier** - Handles complex relationships and reduces overfitting
- **Decision Tree Classifier** - Easy to interpret, useful for understanding key factors
- **XGBoost Classifier** - Optimized boosting algorithm for better accuracy
- **Neural Networks** - Deep learning approach for complex pattern detection

### Model Evaluation Metrics
To assess model performance, various evaluation metrics are used:
- **Accuracy Score**
- **Precision, Recall, and F1-Score**
- **Confusion Matrix**
- **ROC-AUC Score**

## Web Application (Optional)
To enhance usability, the model can be deployed as a web application using **Flask** or **Streamlit**, allowing users to enter medical details and get an estimated prediction instantly.

### Steps to Deploy
1. **Train the machine learning model** and save it using `joblib` or `pickle`
2. **Create a Flask API** that accepts patient data and returns the prediction
3. **Build a front-end UI** with Streamlit or React for user interaction
4. **Deploy the application** on **Heroku, AWS, or Google Cloud**

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Jupyter Notebook (for model training)
- Libraries: Pandas, NumPy, Scikit-learn, Flask/Streamlit

### Steps to Run the Project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Model Training Script**
   ```bash
   python train_model.py
   ```
4. **Run the Web Application** (if included)
   ```bash
   streamlit run app.py
   ```
5. **Test API (if using Flask)**
   ```bash
   python app.py
   ```

## Future Enhancements
- **Integration with wearable health devices** for real-time monitoring
- **Deep learning-based disease risk estimation** using CNNs/RNNs
- **Mobile application** for instant heart disease assessment
- **Advanced predictive analytics** using time-series patient data

## License
This project is Owned by ©Bishal Bhati. Feel free to contribute and Improve it.
