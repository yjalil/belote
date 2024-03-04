import streamlit as st


# Set the background color to green
st.markdown(
    """
    <style>
    section {
        background-color: #15572a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Placeholder for the card on the table
st.write("Card on the table:")
table_card_placeholder = st.empty()

# Placeholders for the players' cards
st.write("Player 1's cards:")
player1_cards_placeholder = st.empty()

st.write("Player 2's cards:")
player2_cards_placeholder = st.empty()

st.write("Player 3's cards:")
player3_cards_placeholder = st.empty()

st.write("Player 4's cards:")
player4_cards_placeholder = st.empty()

if __name__ == "__main__":
    st.write("Belote Game")
