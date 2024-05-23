from sklearn.metrics import accuracy_score

def eval_accuracy (y_pred_eval):
    
    y_eval = [ True,  True, False, False, False,  True, False, False, False,
        True, False,  True,  True, False, False,  True, False, False,
        True,  True,  True, False,  True, False,  True, False, False,
       False,  True, False, False, False,  True, False,  True,  True,
       False, False,  True,  True,  True, False, False,  True, False,
       False,  True, False, False, False, False,  True, False,  True,
        True, False, False, False, False,  True,  True, False, False,
        True,  True,  True, False,  True, False,  True, False, False,
       False, False,  True,  True, False,  True, False, False,  True,
       False,  True,  True,  True, False,  True,  True, False, False,
        True,  True, False,  True,  True, False,  True,  True,  True,
        True, False, False, False,  True,  True, False,  True, False,
        True, False, False, False,  True,  True, False, False,  True,
        True,  True,  True, False,  True,  True,  True, False, False,
       False,  True, False,  True,  True,  True, False, False, False,
       False, False, False, False,  True, False,  True,  True, False,
        True, False,  True,  True, False,  True, False, False,  True,
        True,  True,  True, False, False, False,  True,  True, False,
        True,  True, False, False, False,  True, False, False, False,
       False, False,  True, False,  True, False, False,  True, False,
        True,  True,  True, False,  True, False, False, False, False,
       False,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True, False,  True,  True, False,  True,  True,
       False, False,  True, False,  True,  True,  True,  True,  True,
        True,  True,  True,  True, False, False, False, False,  True,
       False, False, False, False,  True,  True,  True, False, False,
        True, False,  True,  True,  True,  True, False,  True, False,
       False,  True,  True, False,  True, False, False,  True,  True,
        True, False,  True,  True, False,  True,  True, False,  True,
        True,  True,  True,  True,  True,  True,  True,  True, False,
       False, False, False,  True,  True, False, False,  True,  True,
       False,  True,  True,  True,  True,  True,  True, False, False,
        True, False,  True,  True, False, False,  True,  True,  True,
       False,  True, False, False,  True,  True, False, False,  True,
        True,  True,  True, False, False, False, False, False,  True,
       False, False, False, False, False,  True, False,  True, False,
        True,  True, False,  True,  True,  True, False, False,  True,
        True, False, False, False,  True,  True,  True,  True, False,
       False,  True,  True,  True, False,  True, False,  True, False,
       False,  True,  True, False, False, False,  True, False,  True,
       False,  True,  True,  True, False, False, False,  True, False,
       False,  True,  True,  True,  True,  True, False, False, False,
       False,  True, False, False, False, False, False, False,  True,
        True, False,  True, False, False,  True, False,  True, False,
        True, False, False,  True, False,  True,  True, False,  True,
       False,  True, False, False, False,  True, False, False, False,
        True, False, False,  True,  True,  True,  True,  True,  True,
       False,  True, False, False, False, False, False,  True, False,
        True,  True, False, False,  True,  True, False, False,  True,
       False, False,  True, False, False,  True,  True,  True,  True,
       False, False, False, False, False,  True,  True, False, False,
       False,  True, False,  True,  True, False,  True, False, False,
       False, False, False,  True, False,  True, False,  True, False,
       False,  True,  True,  True, False, False, False,  True,  True]
    return accuracy_score(y_eval, y_pred_eval)