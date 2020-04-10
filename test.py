# Purpose - Receive the call for testing a page from the Chrome extension and return the result (SAFE/PHISHING)
# for display. This file calls all the different components of the project (The ML model, features_extraction) and
# consolidates the result.

import joblib
#import features_extraction
import sys
import numpy as np
import initial
#import pickle

#from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME
LOCALHOST_PATH = "C:/xampp/htdocs/"
DIRECTORY_NAME = "Malicious-Web-Content-Detection-Using-Machine-Learning-master"
#pickle.load(f, encoding='latin1')

def get_prediction_from_url(test_url):
    features_test = initial.main(test_url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    #features_test = np.array(features_test).reshape((1, -1))

    #clf = joblib.load('C:/xampp/htdocs/' + 'Malicious-Web-Content-Detection-Using-Machine-Learning-master' + '/classifier/random_forest.pkl')

    #pred = clf.predict(features_test)
    #return int(pred[0])

    return features_test 
    #return 1


def main():
    url = sys.argv[1]
    #print(url)
    prediction = get_prediction_from_url(url)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if prediction == 0:
        # print "The website is safe to browse"
        print("SAFE ")
        
    elif prediction == 1:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")
        
    elif prediction == -1:
        print("SUSPICIOUS")

        # print 'Error -', features_test


if __name__ == "__main__":
    main()


