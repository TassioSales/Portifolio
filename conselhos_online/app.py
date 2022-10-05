import requ
import traceback
import streamlit as st
from py_trans import PyTranslator




def get_random_advice():
    """
    Get random advice from https://api.adviceslip.com/

    Returns:
        str: Random advice
    """
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    return advice

if __name__ == "__main__":
    st.title("Random Advice")
    st.write("Click the button to get a random advice")
    if st.button("Get advice"):
        try:
            advice = get_random_advice()
            st.write(advice)
        except Exception:
            st.error(traceback.format_exc())
