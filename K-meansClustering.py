from sklearn.cluster import KMeans
import numpy as np
X=np.array([[1,2],[1,4],[1,0],[5,8],[6,9],[6,7]])
print("Input Data:",X)
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
labels=kmeans.labels_
centers=kmeans.cluster_centers_
print("Labels:",labels)
print("Centers:",centers)
test=[[0,0]]
pred=kmeans.predict(test)
print("Test:",test)
print("Cluster:",pred)
print("Done")