import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error



def fit_transform(X,X_train,X_test,on_):
    """
    -------------------------------------------------------
    beds_bath_flex_ordi
    -------------------------------------------------------
    Transforms:
    ['beds', 'baths', 'flexs'] to Ordinal Encoder
    ['zip'] to One hot Encoder
    Combine both results 
    Returns: ndarray | X_train_prepared and X_test_preapared
    -------------------------------------------------------
    beds_bath_flex_numerical
    -------------------------------------------------------
    Transforms:
    ['beds', 'baths', 'flexs'] to Numerical
    ['zip'] to One hot Encoder
    Combine both results 
    Returns: ndarray | X_train_prepared and X_test_preapared
    ********************************
    Function can be improved futher!
    ********************************

    """
    if(on_ == 'beds_bath_flex_ordi'):
        CAT_ATTRIBS_ONE_HOT = ['zip']
        CAT_ATTRIBS_ORDINAL = ['beds', 'baths', 'flexs']


        # one hot categorical features
        encoder = OneHotEncoder(categories = "auto",  drop='first')
        # fitting encoder for all X's
        X_encoded = encoder.fit_transform(X[CAT_ATTRIBS_ONE_HOT])
        # transforming X_train and y_tain on top of that
        X_train_encoded = encoder.transform(X_train[CAT_ATTRIBS_ONE_HOT])
        X_test_encoded = encoder.transform(X_test[CAT_ATTRIBS_ONE_HOT])
        # Converting sparse to ndarray
        X_train_encoded = X_train_encoded.toarray()
        X_test_encoded = X_test_encoded.toarray()

        # ordinal categorical features
        ord_encoder = OrdinalEncoder()
        X_train_ord_encoder = ord_encoder.fit_transform(X_train[CAT_ATTRIBS_ORDINAL])
        X_test_ord_encoder = ord_encoder.fit_transform(X_test[CAT_ATTRIBS_ORDINAL])

        # Concating both categories AND returing X_train_prepared and X_test_preapared
        X_train_prep = np.concatenate((X_train_encoded,X_train_ord_encoder),axis=1)
        X_test_prep = np.concatenate((X_test_encoded,X_test_ord_encoder),axis=1)

    
    elif(on_ == 'beds_bath_flex_numerical'):
        NUM_ATTR = ['beds', 'baths', 'flexs']
        CAT_ATTRIBS_ONE_HOT = ['zip']
        # one hot categorical features
        encoder = OneHotEncoder(categories = "auto",  drop='first')
        # fitting encoder for all X's
        X_encoded = encoder.fit_transform(X[CAT_ATTRIBS_ONE_HOT])
        # transforming X_train and y_tain on top of that
        X_train_encoded = encoder.transform(X_train[CAT_ATTRIBS_ONE_HOT])
        X_test_encoded = encoder.transform(X_test[CAT_ATTRIBS_ONE_HOT])
        # Converting sparse to ndarray
        X_train_encoded = X_train_encoded.toarray()
        X_test_encoded = X_test_encoded.toarray()

        # Drop zip from train and test
        X_train.drop(CAT_ATTRIBS_ONE_HOT, axis=1)
        X_test.drop(CAT_ATTRIBS_ONE_HOT, axis=1)

        # Concating both categories AND returing X_train_prepared and X_test_preapared
        X_train_prep = np.concatenate((X_train_encoded,X_train[NUM_ATTR]),axis=1)
        X_test_prep = np.concatenate((X_test_encoded,X_test[NUM_ATTR]),axis=1)

        
    # Print shapes
    print('Training set Shape:'+ str(X_train_prep.shape) )
    print('Testing set Shape:'+ str(X_test_prep.shape) )

    return  (X_train_prep, X_test_prep)

 



