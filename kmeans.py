import random
def dist(a,b):
    res=0
    for i in range(len(a)):
        res+=abs(a[i]-b[i])
    return res

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()
    def add(self,val):
        self.closest_users.add(val)
    def update(self,user_feature_map,num_features_per_user):
        temp=[0 for i in range(num_features_per_user)]
        for i in range(num_features_per_user):
            for each in self.closest_users:
                temp[i]+=user_feature_map[each][i]
        self.location=[i/len(self.closest_users) for i in temp]
    def clear(self):
        self.closest_users = set()

def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)
    Centroids=[]
    for each in inital_centroid_users:
        new=Centroid(user_feature_map[each])
        Centroids.append(new)

    i=0
    while(i<10):
        for (key,val) in user_feature_map.items():
            mini=float('inf')
            for each in Centroids:
                curr=dist(val,each.location)
                if curr<mini:
                    mini=curr
                    idx=each
            idx.add(key)
        for each in Centroids:
            each.update(user_feature_map,num_features_per_user)
            each.clear()

        i+=1
    out=[each.location for each in Centroids]
    return out
    # Write your code here.
    pass
