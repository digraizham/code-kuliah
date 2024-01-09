using Clustering
using Random

# Generate some example data
data = hcat([1 2; 5 8; 1.5 1.8; 8 8; 1 0.6; 9 11]...)

# Specify the number of clusters (K)
k = 2

# Initialize centroids randomly
rng = MersenneTwister(42)  # Setting a seed for reproducibility
initial_centroids = rand(rng, size(data, 1), k)

# Perform K-means clustering
result = kmeans(data, k, init = initial_centroids')

# Get cluster assignments and centroids
labels = assignments(result)
centroids = result.centers'

# Print results
println("Cluster Labels:", labels)
println("Centroids:", centroids)
