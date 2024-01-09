from sklearn.cluster import KMeans
import numpy as np

# Generate some example data
data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])

# Specify the number of clusters (K)
k = 2

# Create a KMeans instance
kmeans = KMeans(n_clusters=k)

# Fit the model to the data
kmeans.fit(data)

# Get cluster assignments and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Print results
print("Cluster Labels:", labels)
print("Centroids:", centroids)
