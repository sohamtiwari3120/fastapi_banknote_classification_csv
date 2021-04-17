import numpy as np
import pickle
import streamlit as st

pickle_in = open('./classifier.pkl', 'rb')
clf = pickle.load(pickle_in)

def make_pred(variance, skewness, curtosis, entropy):
    """a simple function to return only the prediction

    Parameters
    ----------
    variance : float
        variance of note
    skewness : float
        skewness input
    curtosis : float
        curtosis input
    entropy : float
        entropy input

    Returns
    -------
    int
        predicted value 1 - authentic, 0 - unauthentic
    """
    return clf.predict(np.array([variance, skewness, curtosis, entropy]).reshape(1, -1))

def main():
    st.title('Bank Note Authenticator')
    variance = st.text_input('Variance', help='Type Here')
    skewness = st.text_input('Skewness', help='Type Here')
    curtosis = st.text_input('Curtosis', help='Type Here')
    entropy = st.text_input('Entropy', help='Type Here')
    result=''

    if(st.button('Predict')):
        try:
            result = make_pred(float(variance), float(skewness), float(curtosis), float(entropy))
            st.success(f'The output is {result}.')
        except Exception as e:
            st.error(f'ERROR: {e}')

    if(st.button('About')):
        st.text('Lets learn')
        st.text('Built with Streamlit. \u2764\ufe0f')

if __name__ == '__main__':
    main()
