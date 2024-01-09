import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score

# Masukkan Data
data = {'Pembeli': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        'x1': [80, 150, 50, 200, 120, 75, 110, 90, 160, 40],
        'x2': [4, 6, 2, 8, 5, 3, 5, 4, 7, 1]
       }

# Jadikan DataFrame
df = pd.DataFrame(data)

# Inisialisasi k-Means dengan 3 cluster
kmeans = KMeans(n_clusters=3, random_state=42, max_iter=8)

# Mengambil nilai x1 dan x2
df_X = df[['x1', 'x2']]

# Melakukan fitting data
df['Cluster'] = kmeans.fit_predict(df_X)

#plot data and cluster centers with legends
for cluster_label in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == cluster_label]
    plt.scatter(cluster_data['x1'], cluster_data['x2'], label=f'Cluster {cluster_label}')

# Plot decision boundaries
x_min, x_max = df['x1'].min() - 1, df['x1'].max() + 1
y_min, y_max = df['x2'].min() - 1, df['x2'].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contour(xx, yy, Z, alpha=0.8, colors='black', linestyles='dashed', linewidths=1)

# Plot cluster centers
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=50, c='black', label='Centroids')

plt.xlabel('Total belanja per bulan (x1)')
plt.ylabel('Frekuensi kunjungan per bulan (x2)')
plt.title('K-Means Clustering')
plt.legend(loc='upper left')
plt.savefig('hasil_clustering.png')
plt.show()

# Definisikan true label
true_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Kalkulasi ARI
rank_index = adjusted_rand_score(df['Cluster'], true_labels)
print(f'Adjusted Rank Index: {rank_index}')