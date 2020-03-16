import numpy as np 
import pandas as pd 
from scipy.stats import uniform
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor


def build_lasso(alp,X_train,y_train):
    """
    Builds Lasso Regrssion and Calcluates RMSE. 
    Returns Model
    """
    # Training model
    lasso_reg = Lasso(alpha=alp)
    lasso_reg.fit(X_train, y_train)

    calculate_rmse(X_train,y_train,lasso_reg)
    
    # Return the model
    return lasso_reg
    
    
def lasso_random_search(n_iter_,cv_,X_train,y_train):
    """
    Perfroms Grid SearchCV for lasso Regression
    returns best model's parameters
    """
    # unifrom distribution for alhpa  
    param_distribs = {'alpha': uniform(loc=0,scale=1),}
    # simple lasso regression 
    l_reg = Lasso()
    # Random Seacrch CV # CV
    rnd_search_lr = RandomizedSearchCV(l_reg,param_distributions=param_distribs,
                                      n_iter=n_iter_, cv=cv_,scoring='neg_mean_squared_error')

    rnd_search_lr.fit(X_train, y_train)
    return rnd_search_lr.best_params_ 

def build_decision_tree(max_depth_,max_features_,X_train,y_train):
    tree_reg = DecisionTreeRegressor(max_depth=max_depth_,max_features=max_features_)
    tree_reg.fit(X_train, y_train)

    calculate_rmse(X_train,y_train,tree_reg)
    
    # Return the model
    return tree_reg


def calculate_rmse(X_train,y_train,model):
    # RMSE Evaluation
    pred = model.predict(X_train)
    mse = mean_squared_error(y_train, pred)
    rmse = np.sqrt(mse)
    print("Simple RMSE Evaluation Score: "+ str(rmse))

    # RMSE Evaluation using Cross-Validation 
    scores = cross_val_score(model, X_train, y_train,
                             scoring="neg_mean_squared_error", cv=4)
    rmse_scores = np.sqrt(-scores)
    print("Cross Valdiation RMSE Evaluation Mean Score: "+ str(np.mean(rmse_scores)))