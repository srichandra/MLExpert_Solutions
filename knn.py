# Should use the `find_k_nearest_neighbors` function below.
def get_dist(a,b):
    res=0
    import math
    for i in range(len(a)):
        res+=((a[i]-b[i])**2)
    return math.sqrt(res)
def predict_label(examples, features, k, label_key="is_intrusive"):
    res=find_k_nearest_neighbors(examples, features, k)
    res_labels=[examples[pid]['is_intrusive'] for pid in res]
    return round(sum(res_labels)/k)
    pass


def find_k_nearest_neighbors(examples, features, k):
    res={}
    for (i,j) in examples.items():
        dist=get_dist(features,j['features'])
        res[i]=[dist,j['is_intrusive']]
    res=dict(sorted(res.items(),key = lambda x:x[1][0]))
    out=list(res.keys())[:k]
    return out
    pass
