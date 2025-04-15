# CyberSentinel Security Solutions - Anomaly Detection System
**Authors:** Archana Suresh Patil & Tommy Barron  
**Course:** ADS 508: Data Science with Cloud Computing  
**Instructor:** Sean Coyne  
**Institution:** University of San Diego - Shirley Marcos School of Engineering  
**Date:** April 14, 2025  

## Project Overview

CyberSentinel Security Solutions presents a real-time **Anomaly Detection System** to detect **DDoS attacks** and other cybersecurity threats using machine learning. The solution integrates AWS Cloud services with advanced modeling techniques to analyze network traffic patterns and provide high-accuracy threat detection.

## Problem Statement

Traditional rule-based systems are ineffective against evolving cyber threats. Our project addresses this gap by building a scalable ML pipeline to identify abnormal patterns in real-time traffic data, focusing on:
- DDoS attacks
- Unauthorized access
- Insider threats

---

## Goals

- Detect anomalies with **≥ 90% accuracy**
- Maintain **< 5% false positive rate**
- Reduce alert response time by **30%**

---

## Non-Goals

- Creating a fully autonomous security system
- Addressing legal/regulatory compliance
- Covering all types of cyberattacks

---

## Data Sources

- **UNSW-NB15 Dataset** ([Kaggle](https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15))
- **CIC-DDoS 2019 Dataset** ([Kaggle](https://www.kaggle.com/datasets/aymenabb/ddos-evaluation-dataset-cic-ddos2019))
- **Canadian Institute for Cybersecurity (2016-2018)** ([Kaggle](https://www.kaggle.com/datasets/devendra416/ddos-datasets))

Stored and processed using:
- **AWS S3**: `s3://msads-508-sp25-team6`
- **SageMaker Studio**

---

##  Models & Techniques

- **Random Cut Forest**
- **Autoencoder Neural Networks**
- **Isolation Forest**
- **XGBoost**
- **Dimensionality Reduction** (PCA, t-SNE, LDA)
- **SMOTE** for class balancing
- One-hot encoding and custom feature engineering

---

##  Cloud Infrastructure

- **AWS SageMaker:** Custom bring-your-own-script (Scikit-learn, Keras, XGBoost)
- **Instance types:** `ml.m5.2xlarge`
- **Model tracking:** CloudWatch & MLflow
- **Real-time streaming (planned):** Apache Kafka

---

## Evaluation Metrics

- Precision, Recall, F1-Score
- ROC-AUC
- Reconstruction Error (Autoencoders)
- Outlier Score Distribution

---

## Privacy & Security

- No PII/PHI data used
- Anonymized network traffic
- Ethical concerns noted and mitigated
- Bias handled via class weighting and sampling

---

## Future Enhancements

- Integrate **AWS Redshift** for storage efficiency
- Add features like:
  - Entropy detection
  - Geo-IP mapping
  - Burst packet monitoring
- Introduce **hybrid model pipelines** with KNN & SGD
- Feedback loop from analysts for continuous improvement
