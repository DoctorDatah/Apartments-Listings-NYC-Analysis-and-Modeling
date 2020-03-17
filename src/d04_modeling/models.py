import numpy as np 
import pandas as pd 
from scipy.stats import uniform
from sklearn.svm import LinearSVR
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import AdaBoostRegressor


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


def build_svm(epsilon_,C_,X_train,y_train):
    tree_reg = LinearSVR(epsilon=epsilon_, C=C_)
    tree_reg.fit(X_train, y_train)

    calculate_rmse(X_train,y_train,tree_reg)
    
    # Return the model
    return tree_reg

def svm_random_search(n_iter_,cv_,X_train,y_train):
    """
    Perfroms Grid SearchCV for SVM Regression
    returns best model's parameters
    """
    # unifrom distribution for epsilon  
    param_distribs = {'epsilon': uniform(loc=0,scale=4),
                     'C': uniform(loc=0,scale=100)}
    # SVR regression 
    l_reg = LinearSVR()
    # Random Seacrch CV # CV
    rnd_search_lr = RandomizedSearchCV(l_reg,param_distributions=param_distribs,
                                      n_iter=n_iter_, cv=cv_,scoring='neg_mean_squared_error')

    rnd_search_lr.fit(X_train, y_train)
    return rnd_search_lr.best_params_ 


def build_ensemble(X_train,y_train):
    """
    Bulid's ensmble on the best paramters of Lasso, Random Forest, Decision Tree, SVM
    """
    # Lasso Regression
    lasso_reg = Lasso(alpha=0.35) # alpha from RandomSearch
    #  Random Foresst
    rnd_reg = RandomForestRegressor(n_estimators=100)
    # Decision Tree
    tree_reg = DecisionTreeRegressor(max_depth=40,max_features=5)
    # SVM
    svm_reg = LinearSVR(1.5,31)
    # Voting Regressor 
    voting_reg1 = VotingRegressor(
        estimators=[('lr', lasso_reg), ('rf', rnd_reg), ('tree', tree_reg),('svm', svm_reg)])

    voting_reg1.fit(X_train, y_train)
    calculate_rmse(X_train,y_train,voting_reg1)
    return voting_reg1


def calculate_rmse(X_train,y_train,model):

    scores = cross_val_score(model, X_train, y_train,
                             scoring="neg_mean_squared_error", cv=4)
    rmse_scores = np.sqrt(-scores)
    print("Cross Valdiation RMSE Evaluation Mean Score: "+ str(np.mean(rmse_scores)))