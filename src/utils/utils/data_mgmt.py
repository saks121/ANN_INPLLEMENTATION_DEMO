import tensorflow as tf



def get_data(validation_datasize):
    mnist =tf.keras.datasets.mnist
    (X_train_full, y_train_full), (X_test,y_test) = mnist.load_data()
    # create a validation dataset from full trg.data
    # scale the data b/w 0-1 by dividing the data points by 255.as its an unsigned data b/w the rnage 0-255

    X_valid, X_train =X_train_full[:validation_datasize] /255., X_train_full[validation_datasize:] /255.
    y_valid, y_train =y_train_full[:validation_datasize] /255., y_train_full[validation_datasize:]

    # scale the test dataset
    X_test =X_test /255.
    return (X_train,y_train), (X_valid,y_valid), (X_test,y_test)