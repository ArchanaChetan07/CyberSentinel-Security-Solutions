import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


class TestNetworkDataProcessing:

    def test_ip_feature_extraction(self):
        df = pd.DataFrame({"src_bytes": [1000, 5000, 200000], "dst_bytes": [500, 1000, 100000]})
        df["total_bytes"] = df["src_bytes"] + df["dst_bytes"]
        assert df["total_bytes"].tolist() == [1500, 6000, 300000]

    def test_missing_values_imputed(self):
        df = pd.DataFrame({"duration": [0.5, None, 1.2, None], "label": ["normal", "attack", "normal", "attack"]})
        df["duration"] = df["duration"].fillna(df["duration"].median())
        assert df["duration"].isnull().sum() == 0

    def test_label_encoding(self):
        labels = pd.Series(["normal", "attack", "normal", "ddos"])
        encoded = pd.Categorical(labels).codes
        assert len(set(encoded)) == 3

    def test_feature_scaling(self):
        X = np.array([[100, 1000], [200, 500], [50, 2000]])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        assert abs(X_scaled[:, 0].mean()) < 1e-10


class TestAnomalyDetection:

    def test_isolation_forest_detects_anomalies(self):
        np.random.seed(42)
        normal = np.random.randn(200, 5) * 0.5
        anomalies = np.random.randn(10, 5) * 10
        X = np.vstack([normal, anomalies])
        model = IsolationForest(contamination=0.05, random_state=42)
        preds = model.fit_predict(X)
        assert -1 in preds

    def test_classifier_accuracy_above_baseline(self):
        np.random.seed(42)
        X = np.random.rand(300, 10)
        y = (X[:, 0] + X[:, 1] > 1.0).astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=20, random_state=42)
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        assert acc > 0.6

    def test_prediction_labels_valid(self):
        np.random.seed(0)
        X = np.random.rand(100, 5)
        y = np.random.randint(0, 2, 100)
        model = RandomForestClassifier(n_estimators=5, random_state=0)
        model.fit(X, y)
        preds = model.predict(X)
        assert set(preds).issubset({0, 1})
