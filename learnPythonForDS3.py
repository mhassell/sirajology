import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# fetch data and format it
data = fetch_movielens(min_rating = 4.0)

# print info about training and test data
print repr(data['train'])
print repr(data['test'])

# create model
model = LightFM(loss='warp')
# train model
model.fit(data['train'], epochs=30, num_threads=1)

def sample_recommendation(model, data, user_ids):
    
    # number of users and movies in training data
    n_users, n_items = data['train'].shape

    # generate recs for each user
    for user_id in user_ids:

        # movies they liked
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # movies we predict they will like
        scores = model.predict(user_id,np.arange(n_items))

        # sort in order from most liked to least liked
        top_items = data['item_labels'][np.argsort(-scores)]

        # print the results
        print "User %s " % user_id
        print "          Known positives:"

        for x in known_positives[:3]:
            print("           %s" % x)

        print "          Best recommendations:"

        for x in top_items[:3]:
            print("           %s" % x)

sample_recommendation(model,data,[5, 10, 50])
