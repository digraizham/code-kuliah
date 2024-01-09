import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 1. Baca data
data = pd.read_csv('07DataSet_LDA_Training.csv')

# 2. Bagi data menjadi 80% untuk training dan 20% untuk evaluasi
train_data, eval_data = train_test_split(data, test_size=0.2, random_state=42)

# 2. Membangun dua model klasifikasi SVM
# i. Linear-SVM
linear_svm = SVC(kernel='linear')

target_column = 'Prime_Sport'
if target_column in train_data.columns:
    linear_svm.fit(train_data.drop(target_column, axis=1), train_data[target_column])
else:
    print(f"Error: '{target_column}' column not found in train_data")

# ii. Kernel-SVM (gunakan kernel yang sesuai, misalnya 'rbf')
kernel_svm = SVC(kernel='rbf')
kernel_svm.fit(train_data.drop(target_column, axis=1), train_data[target_column])

# 3a. Evaluasi kinerja
eval_predictions_linear = linear_svm.predict(eval_data.drop(target_column, axis=1))
eval_predictions_kernel = kernel_svm.predict(eval_data.drop(target_column, axis=1))

accuracy_linear = accuracy_score(eval_data[target_column], eval_predictions_linear)
accuracy_kernel = accuracy_score(eval_data[target_column], eval_predictions_kernel)

print(f'Linear-SVM Accuracy: {accuracy_linear}')
print(f'Kernel-SVM Accuracy: {accuracy_kernel}')

# 3b. Model manakah yang terbaik
best_model = "Linear-SVM" if accuracy_linear > accuracy_kernel else "Kernel-SVM"
print(f'The best model is: {best_model}')

# 4. Deployment
scoring_data = pd.read_csv('07DataSet_LDA_Scoring.csv')
scoring_predictions = linear_svm.predict(scoring_data)

# Tambahkan hasil prediksi ke dalam DataFrame
scoring_data['predicted_target'] = scoring_predictions

# Simpan hasil deployment ke file jika diperlukan
scoring_data.to_csv('hasil_deployment.csv', index=False)
