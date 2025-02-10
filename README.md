# 🔥 Algerian Forest Fire Prediction Project  

This project predicts **forest fires** in Algeria using a public dataset from two regions: **Bejaia** (Northeast) and **Sidi Bel-Abbes** (Northwest). The dataset contains weather observations and fire data collected between **June 2012 and September 2012**.  

---

## 🛠️ Tech Stack
- Python 🐍
- Pandas & NumPy for data processing
- Matplotlib & Seaborn for visualization
- Scikit-learn for model training
- Flask for web development

---

## 📂 Dataset Overview  
The dataset includes **244 instances**, divided into:  
- 🔥 **Fire**: 138 instances  
- 🌿 **Not Fire**: 106 instances  

### **Attributes:**  
1. 📅 **Date**: Day, month, year (June–September 2012)  
2. 🌡️ **Temp**: Temperature at noon (22°C to 42°C)  
3. 💧 **RH**: Relative Humidity (21% to 90%)  
4. 🌬️ **Ws**: Wind speed (6 km/h to 29 km/h)  
5. 🌧️ **Rain**: Total rain in mm (0 to 16.8)  
6. 🔥 **FWI Components** (Fine Fuel Moisture, Duff Moisture, Drought Code, etc.)  

---

## 🚀 Project Workflow  
1. **Data Cleaning** 🧹  
   - Handled missing values, formatted the data, and standardized features.  

2. **Exploratory Data Analysis (EDA)** 📊  
   - Visualized relationships between attributes and their impact on fire occurrence.  

3. **Feature Engineering & Selection** 🛠️  
   - Extracted key features for better model performance.  

4. **Model Training** 🤖  
   - Trained the following regression models:  
     - **Linear Regression**  
     - **Ridge Regression**  
     - **Lasso Regression**  
     - **ElasticNet Regression**  

5. **Model Serialization** 📦  
   - Saved the best model using **pickle** for deployment.  

6. **Web Application with Flask** 🌐  
   - Built a user-friendly web interface to make predictions based on input data.
     <img width="1687" alt="Screenshot 2025-01-19 at 7 53 05 PM" src="https://github.com/user-attachments/assets/01e84f81-96dd-434d-94c8-9af41f083f4c" />



7. **Deployment** 🚀  
   - Deployed the Flask application for usage.
   <img width="1681" alt="Screenshot 2025-01-19 at 7 53 49 PM" src="https://github.com/user-attachments/assets/a4372d0e-6274-484e-bd15-35bde228ddba" />
 

---

## 📊 Results  
- Achieved 98% in predicting forest fire occurrences.  
- Successfully created a dynamic web app for predictions.  

---

## 🛠️ How to Use  
1. Clone this repository:  
   ```bash
   git clone https://github.com/Ganglet/Algerian-Forest-Fire-Model.git

---

## 📬 Contact
Feel free to reach out if you have any questions or suggestions!

- Email: angshumanchakravertty2@gmail.com
- GitHub: https://github.com/Ganglet


   
