import panphon.distance
dst = panphon.distance.Distance()
def feature_edit_distance2(source, target, xsampa=False):
    return dst.min_edit_distance(unweighted_deletion_cost2,
                                      unweighted_insertion_cost2,
                                      dst.unweighted_substitution_cost,
                                      [[]],
                                      dst.fm.word_to_vector_list(source, numeric=True),
                                      dst.fm.word_to_vector_list(target, numeric=True))

def unweighted_deletion_cost2(v1, gl_wt=0.5):
    """Return cost of deleting segment corresponding to feature vector
    Features are not weighted; features specified as '0' add 0.5 to the raw
    deletion cost; other features add 1 to the raw deletion cost; the cost
    is normalized by the number of features
    Args:
        v1 (list): vector of feature values
        global_weight (Number): global weighting factor
    Returns:
        float: sum of feature costs divided by the number of features and
               multiplied by a global weighting factor
        """
    assert isinstance(v1, list)
    return sum(map(lambda x: 0.5 if x == 0 else 1, v1)) / len(v1) * gl_wt

def unweighted_insertion_cost2(v1, gl_wt=0.5):
    """Return cost of inserting segment corresponding to feature vector
        Features are not weighted; features with the value '0' add 0.5 to the
        raw cost; other features add 1.0 to the raw cost; the raw cost is then
        normalized by the number of features
        Args:
            v1 (list): vector of feature values
            global_weight (Number): global weighting factor
        Returns:
            float: sum of the costs of inserting each of the features in `v1`
                   divided by the number of features in the vector and
                   multiplied by a global weighting factor
        """
    return sum(map(lambda x: 0.5 if x == 0 else 1, v1)) / len(v1) * gl_wt
    
