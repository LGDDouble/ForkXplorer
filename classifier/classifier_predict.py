from sklearn.externals import joblib

def predict(test_data):
    RF = joblib.load('rf.model')
    result = RF.predict(test_data)
    return result

