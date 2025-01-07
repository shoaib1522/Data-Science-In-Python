import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, precision_recall_curve, auc
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import os

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv('creditcard.csv')

data = load_data()

# Sidebar options
st.sidebar.title("Credit Card Fraud Detection")
option = st.sidebar.radio("Navigate the App:", ["Introduction", "EDA", "Model Training", "Transaction Prediction", "Conclusion"])

# Global Preprocessing Step
st.write("### Data Preprocessing (Global)")
X = data.drop(columns=['Class'])
y = data['Class']

# Define and fit the scaler globally
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset globally
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define a function to build and train the model
@st.cache_resource
def build_and_train_model():
    model = Sequential([
        Dense(128, input_dim=X_train.shape[1], activation='relu'),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, validation_split=0.2, epochs=10, batch_size=32, verbose=0)
    return model

# Train the model once and save it globally
if 'model' not in st.session_state:
    st.session_state.model = build_and_train_model()

model = st.session_state.model  # Retrieve the model for prediction

if option == "Introduction":
    st.title("Credit Card Fraud Detection")
    st.markdown("""
    - **Dataset**: 284,807 transactions with only 492 labeled as fraud.
    - **Objective**: Detect fraudulent transactions using machine learning.
    - **Features of the App**:
        1. Explore the dataset with interactive visualizations.
        2. Train and evaluate a Multi-Layer Perceptron (MLP) model.
        3. Predict fraud for custom transaction inputs.
    """)

elif option == "EDA":
    st.title("Exploratory Data Analysis")
    st.write("### Dataset Overview")
    st.dataframe(data.head())
    st.write("### Summary Statistics")
    st.write(data.describe())

    st.write("### Class Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='Class', data=data, palette='Set1', ax=ax)
    st.pyplot(fig)

    st.write("### Transaction Amount Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data['Amount'], bins=50, kde=True, color='blue', ax=ax)
    st.pyplot(fig)

elif option == "Model Training":
    st.title("Machine Learning Model Training")
    st.write("Model has been trained and is ready for evaluation.")

    st.write("### Model Evaluation")
    y_pred = (model.predict(X_test) > 0.5).astype(int)
    report = classification_report(y_test, y_pred, output_dict=True)
    st.json(report)

    precision, recall, thresholds = precision_recall_curve(y_test, model.predict(X_test))
    auc_pr = auc(recall, precision)
    st.write(f"Area Under Precision-Recall Curve: {auc_pr:.4f}")
    fig, ax = plt.subplots()
    ax.plot(recall, precision, label=f'AUPRC = {auc_pr:.4f}')
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.legend()
    st.pyplot(fig)

elif option == "Transaction Prediction":
    st.title("Transaction Prediction")

    st.write("### Input Transaction Details")
    user_input = {}
    for col in data.columns[:-1]:  # Exclude 'Class'
        user_input[col] = st.number_input(f"{col}", value=0.0)

    st.write("### Predict Fraud")
    input_data = pd.DataFrame([user_input])
    scaled_input = scaler.transform(input_data)  # Use the global scaler here
    prediction = model.predict(scaled_input)
    fraud_probability = prediction[0][0]
    st.write(f"Fraud Probability: {fraud_probability:.2f}")
    if fraud_probability > 0.5:
        st.error("This transaction is likely fraudulent!")
    else:
        st.success("This transaction is likely legitimate.")

elif option == "Conclusion":
    st.title("Conclusion")
    st.markdown("""
    - The MLP model performs well in detecting fraudulent transactions, achieving a high AUPRC.
    - Imbalanced datasets require careful handling to ensure model effectiveness.
    - Real-world applications can benefit from deploying this model in production systems.
    - Future work can include hyperparameter tuning and testing additional algorithms.
    """)
