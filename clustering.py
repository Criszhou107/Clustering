# Some helpful functions

def GetLeafIndices(i, N, Z):
    ''' Recursive function to find leaf index '''
    if(i < N):
        return int(i)
    else:
        il = Z[i - N, :2]
        return [GetLeafIndices(int(im), N, Z) for im in il]
import collections 
def flatten(x):
    ''' Flatten list '''
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]
def GetClusters(Z, X, threshold):
    import numpy as np
    ''' Get clusters at hierarchical level defined by threshold.
    X is data matrix, Z is linkage. '''
    N = X.shape[0]
    # All indices idx >= len(X) actually refer to the cluster formed in Z[idx - len(X)].
    # Zthreshold = Z[Z[:, 2] < 0.059, :]  # get all Z under threshold
    # ll = np.asarray(flatten(GetLeafIndices(280, N, Zthreshold)))  # list of lists
    Zthreshold = Z[Z[:, 2] < threshold, :]  # get all Z under threshold
    indCluster = np.arange(N)  # assign each point to its own clusterIrisCluster_interactive
    for iz in range(Zthreshold.shape[0]):
        z = Zthreshold[int(iz), :]
        l1 = flatten(GetLeafIndices(int(z[0]), N, Zthreshold)) 
        l2 = flatten(GetLeafIndices(int(z[1]), N, Zthreshold))
        l = l1+l2
        m = int(indCluster[l].min())
    #     print(iz, l, m)
        indCluster[l] = m
    cId = np.ones_like(indCluster)
    for ii, i in enumerate(np.unique(indCluster)):
        cId[indCluster == i] = ii
#     np.unique(cId)
    return cId
    
# The main function returning the dendogram
    
def Dendogram(data, method='ward', metric='euclidean', distanceThreshold=0.3):
    if(method in ['‘centroid’, ‘median’,‘ward’'] and metric != 'euclidean'):
        raise NameError('Methods ‘centroid’, ‘median’ and ‘ward’ are correctly defined only if Euclidean pairwise metric is used.') 
    
    import matplotlib.pyplot as plt
    from scipy.cluster.hierarchy import dendrogram, linkage
    
    X = data.values.copy()
    Z = linkage(X, method=method, metric=metric)
    Z[:, 2] = Z[:, 2] / Z[:, 2].max()  # distance in [0, 1]
    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
        color_threshold=distanceThreshold,
    )
    ax = plt.gca()
    ax.tick_params(axis='y', which='major', labelsize=20)  
    ax.set_ylabel('Distance', fontsize=20)  
    ax.set_xlabel('Sample Index', fontsize=20)  
    ax.set_title('Hierarchical Clustering Dendrogram', fontsize=20)  
    plt.axhline(y=distanceThreshold, c='k')
    plt.show() # Show the dendogram
    clusters = GetClusters(Z.copy(), X.copy(), distanceThreshold) # Return the cluster membership
    return clusters

