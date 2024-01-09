import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score

#Memasukkan data
data = {'Pembeli': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        'x1': [80, 150, 50, 200, 120, 75, 110, 90, 160, 40],
        'x2': [4, 6, 2, 8, 5, 3, 5, 4, 7, 1]
       }

#Jadikan DataFrame
df = pd.DataFrame(data)

#Cek apakah data sudah masuk dan menjadi DataFrame
df.head(len(df))

# Mengambil nilai x1 dan x2
X = df[['x1', 'x2']]

# Inisialisasi k-Means dengan 3 cluster
kmeans = KMeans(n_clusters=3, init='random', random_state=42, n_init='auto', max_iter=10)

# Melakukan fitting data
model = kmeans.fit(X)

df['Cluster'] = model.predict(X)
df

#Cek DataFrame terbaru
df.head(len(df))

# Plot data and cluster centers with legends
for cluster_label in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == cluster_label]
    plt.scatter(cluster_data['x1'], cluster_data['x2'], label=f'Cluster {cluster_label}')

# Membuat garis pembatas antar cluster (Dalam hal ini saya buat secara manual)
plt.plot([40, 200], [2.5, 2.5], color='black', linestyle='-', linewidth=1)
plt.plot([40, 200], [5.5, 5.5], color='black', linestyle='-', linewidth=1)

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=50, c='black', label='Centroids')
plt.xlabel('Total belanja per bulan (x1)')
plt.ylabel('Frekuensi kunjungan per bulan (x2)')
plt.title('K-Means Clustering')
plt.legend(loc='upper left')
plt.show()

# Definisikan true label
true_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Kalkulasi ARI
ari = adjusted_rand_score(df['Cluster'], true_labels)
print(f'Adjusted Rand Index: {ari}')