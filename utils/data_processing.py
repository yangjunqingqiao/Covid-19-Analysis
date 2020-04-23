from sklearn.cluster import KMeans

# Class wrapper to store, process, and plot data
class prepared_data:
    def __init__(self, data, estimator=KMeans(init='k-means++', n_clusters=2, n_init=10)):
        self.data = data
        self.estimator = estimator

    # minus mean, divide by std
    def normalized(self):
        return scale(self.data)
    
    def plot(self):
        pass