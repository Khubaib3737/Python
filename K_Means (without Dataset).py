import numpy as np

def kmeans(X, k, max_iters=1000):
    """
    K-means clustering algorithm

    Parameters:
    X (numpy array): data points, shape (n_samples, n_features)
    k (int): number of clusters
    max_iters (int): maximum number of iterations

    Returns:
    centroids (numpy array): cluster centroids, shape (k, n_features)
    labels (numpy array): cluster labels, shape (n_samples,)
    """
    # Initialize centroids randomly
    centroids = np.random.rand(k, X.shape[1])

    # Initialize labels
    labels = np.zeros(X.shape[0], dtype=int)

    for _ in range(max_iters):
        # Assign each data point to the closest centroid
        for i, x in enumerate(X):
            distances = np.linalg.norm(x - centroids, axis=1)
            labels[i] = np.argmin(distances)

        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

# Example usage
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
k = 2
centroids, labels = kmeans(X, k)
print("Centroids:", centroids)
print("Labels:", labels)