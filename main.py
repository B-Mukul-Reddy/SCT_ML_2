import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('Mall_Customers.csv')

# Select relevant features for clustering
features = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Function to plot the Elbow Method to determine the optimal number of clusters
def plot_elbow(scaled_data, max_k=10):
    wcss = []
    for i in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(scaled_data)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_k + 1), wcss, marker='o', linestyle='-', color='b')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS (Within-Cluster Sum of Square)')
    plt.xticks(range(1, max_k + 1))
    plt.show()

# Plot the Elbow Method to determine optimal clusters
plot_elbow(scaled_features)

# Define optimal k based on the Elbow Method observation (e.g., 5 clusters)
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
labels = kmeans.fit_predict(scaled_features)

# Add the cluster labels to the original data
data['Cluster'] = labels

# Print the number of data points in each cluster
for cluster in range(optimal_k):
    print(f"Number of data points in Cluster {cluster}: {sum(data['Cluster'] == cluster)}")

# Visualize the clusters with color coding and legends
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    data['Annual Income (k$)'], 
    data['Spending Score (1-100)'], 
    c=data['Cluster'], 
    cmap='viridis', 
    s=50,
    edgecolor='k'
)
plt.title('Customer Clusters Based on Annual Income and Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.colorbar(scatter, label='Cluster Label')
plt.show()
