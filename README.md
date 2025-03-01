# Algerian Forest Fire Prediction Project

## Project Overview
**Objective:**  
Develop a predictive model to forecast forest fires in Algeria using historical weather and fire data. The project focuses on two regions – **Bejaia** (Northeast) and **Sidi Bel-Abbes** (Northwest) – with data collected from June 2012 to September 2012.

**Key Achievements:**  
- Achieved **98% accuracy** in predicting forest fire occurrences.
- Deployed a **Flask**-based web application for real-time predictions.
- Utilized multiple regression techniques for robust model performance.

---

## Technologies & Tools
- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning Models:** Linear Regression, Ridge, Lasso, ElasticNet (using Scikit-learn)
- **Web Development:** Flask
- **Model Serialization:** Pickle

---

## Dataset Overview
- **Total Instances:** 244  
  - **Fire:** 138 instances  
  - **Not Fire:** 106 instances  
- **Data Collection Period:** June 2012 – September 2012  
- **Key Attributes:**
  - **Date:** Day, month, and year information.
  - **Temp:** Temperature at noon (22°C to 42°C).
  - **RH:** Relative Humidity (21% to 90%).
  - **Ws:** Wind Speed (6 km/h to 29 km/h).
  - **Rain:** Total rainfall in mm (0 to 16.8 mm).
  - **FWI Components:** Includes metrics like Fine Fuel Moisture, Duff Moisture, Drought Code, etc.

---

## Methodology & Workflow
1. **Data Cleaning & Preprocessing**
   - Handled missing values and standardized features.
   - Transformed raw data for effective modeling.

2. **Exploratory Data Analysis (EDA)**
   - Visualized attribute distributions and correlations using Seaborn and Matplotlib.
   - Identified key predictors affecting fire occurrences.

3. **Feature Engineering & Selection**
   - Extracted and selected features to enhance model performance.
   - Applied statistical techniques to validate feature importance.

4. **Model Training & Evaluation**
   - Implemented and compared several regression models:
     - **Linear Regression**
     - **Ridge Regression**
     - **Lasso Regression**
     - **ElasticNet Regression**
   - Evaluated models using metrics like Mean Squared Error (MSE) and R².

5. **Model Serialization**
   - Serialized the best performing model with Pickle for deployment.

6. **Web Application Development**
   - Developed a user-friendly Flask web app to allow users to input data and receive real-time predictions.
   - Integrated interactive data visualizations within the web interface.

7. **Deployment**
   - Deployed the Flask application on a cloud platform for accessibility.
   - Ensured scalability and responsiveness in the production environment.

---

## Visual Demonstrations
### Web Application Interface
![Flask Web App Screenshot](https://github.com/user-attachments/assets/01e84f81-96dd-434d-94c8-9af41f083f4c)

### Model Prediction Dashboard
![Prediction Dashboard Screenshot](https://github.com/user-attachments/assets/a4372d0e-6274-484e-bd15-35bde228ddba)

---

## Results & Impact
- **Accuracy:** 98% in predicting forest fires.
- **Real-Time Predictions:** Enabled dynamic forecasting via the deployed web app.
- **Business Impact:** Provides a tool for early warning systems, potentially reducing forest fire damage and aiding in resource allocation.

---

## How to Get Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ganglet/Algerian-Forest-Fire-Model.git
