import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs, make_moons
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

def visualize_clusters_2d(X, labels, centers=None, title="Clusters"):
    plt.figure(figsize=(10, 7))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
    if centers is not None:
        plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    return plt.gcf()

def visualize_clusters_3d(X, labels, centers=None, title="Clusters"):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, s=50, cmap='viridis')
    if centers is not None:
        ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='red', s=200, alpha=0.75)
    ax.set_title(title)
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.set_zlabel("Feature 3")
    return plt.gcf()

def calculate_cluster_statistics_kmeans(X, labels, centers):
    unique_labels = np.unique(labels)
    stats = []
    for label in unique_labels:
        cluster_points = X[labels == label]
        num_points = len(cluster_points)
        center = centers[label]
        stats.append({
            'cluster': label,
            'num_points': num_points,
            'center': center
        })
    return stats

def calculate_cluster_statistics_dbscan(X, labels):
    unique_labels = np.unique(labels)
    stats = []
    for label in unique_labels:
        if label == -1:
            continue  # Ignore noise
        cluster_points = X[labels == label]
        num_points = len(cluster_points)
        density = num_points / (np.max(cluster_points, axis=0) - np.min(cluster_points, axis=0)).prod()
        stats.append({
            'cluster': label,
            'num_points': num_points,
            'density': density
        })
    return stats

def launch_cluster_knn(df, array_columns, n=3, dimensions=2):
    X = df[array_columns].values
    if len(array_columns) > 3:
        pca = PCA(dimensions)
        X = pca.fit_transform(df)
    
    kmeans = KMeans(n_clusters=n, random_state=42)
    labels_kmeans = kmeans.fit_predict(X)
    centers_kmeans = kmeans.cluster_centers_
    # for stat in stats_kmeans:
    #     print(f"Cluster {stat['cluster']}: {stat['num_points']} points, Center: {stat['center']}")

    stats_kmeans = calculate_cluster_statistics_kmeans(X, labels_kmeans, centers_kmeans)
    if dimensions == 3:
        return visualize_clusters_3d(X, labels_kmeans, centers_kmeans, title="K-Means Clustering 3D")
    else:
        return visualize_clusters_2d(X, labels_kmeans, centers_kmeans, title="K-Means Clustering")

def launch_cluster_dbscan(df, array_columns, dimensions=2):
    X = df[array_columns].values
    if len(array_columns) > 3:
        pca = PCA(dimensions)
        X = pca.fit_transform(df)
    
    dbscan = DBSCAN(eps=0.2, min_samples=5)
    labels_dbscan = dbscan.fit_predict(X)
    stats_dbscan = calculate_cluster_statistics_dbscan(X, labels_dbscan)
    # for stat in stats_dbscan:
    #     print(f"Cluster {stat['cluster']}: {stat['num_points']} points, Density: {stat['density']}")
    if dimensions == 3:
        return visualize_clusters_3d(X, labels_dbscan, title="DBSCAN Clustering 3D")
    else:
        return visualize_clusters_2d(X, labels_dbscan, title="DBSCAN Clustering")
    return stats_dbscan

def launch_cluster(df, array_columns):
    X = df[array_columns].values
    
    kmeans = KMeans(n_clusters=4, random_state=42)
    labels_kmeans = kmeans.fit_predict(X)
    centers_kmeans = kmeans.cluster_centers_
     
    stats_kmeans = calculate_cluster_statistics_kmeans(X, labels_kmeans, centers_kmeans)
    # for stat in stats_kmeans:
    #     print(f"Cluster {stat['cluster']}: {stat['num_points']} points, Center: {stat['center']}")

    # Appliquer DBSCAN
    dbscan = DBSCAN(eps=0.2, min_samples=5)
    labels_dbscan = dbscan.fit_predict(X)
    stats_dbscan = calculate_cluster_statistics_dbscan(X, labels_dbscan)
        # for stat in stats_dbscan:
        #     print(f"Cluster {stat['cluster']}: {stat['num_points']} points, Density: {stat['density']}")
    if len(array_columns) == 3:
        visualize_clusters_3d(X, labels_kmeans, centers_kmeans, title="K-Means Clustering 3D")
        visualize_clusters_3d(X, labels_dbscan, title="DBSCAN Clustering 3D")
    else:
        visualize_clusters_2d(X, labels_kmeans, centers_kmeans, title="K-Means Clustering")
        visualize_clusters_2d(X, labels_dbscan, title="DBSCAN Clustering")
    return stats_kmeans,stats_dbscan
    
