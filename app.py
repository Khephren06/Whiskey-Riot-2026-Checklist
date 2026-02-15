import streamlit as st

st.set_page_config(
    page_title="Whiskey Riot 2026 Checklist",
    page_icon="🥃",
    layout="wide",
)

st.logo("https://raw.githubusercontent.com/Khephren06/Whiskey-Riot-2026-Checklist/refs/heads/main/IMG_0259.jpeg")

st.title("Whiskey Riot 2026 Checklist")
st.write(
    "Check off each drink as you try it, add tasting notes, and record your cigar pairings. "
    "Each person’s data is saved in their own browser session."
)

# ---------- DATA ----------

sections = {
    "FIRST POUR & GLASSWARE": [
        "Brother's Bond Straight Bourbon Whiskey",
    ],
    "OFFICIAL COCKTAIL BARS": [
        "Luxco Portfolio - Penelope & Yellowstone",
        "Cutty Sark - Ginger & Scotch",
    ],
    "EARLY ENTRY POURS": [
        "James E. Pepper 'Decanter' Rye Barrel Proof",
        "Pursuit Spirits Triple Mash Bourbon and Rye (Barrel Proof)",
        "Starlight Honey Reserve",
        "Bending Branch 1840 Culinaria Private Barrel Bourbon Blend",
        "Balcones Cataleja",
        "Balcones Mirador",
        "Blue Note - Limited Product TBD",
        "Chicken Cock Miller's Reserve American Whiskey",
        "Still Austin DRS",
        "Augusta KY Distillery - Buckner's 13",
        "St. George Single Malt Whiskey - Lot Series",
        "Jimmy Red Wheated Bourbon Whiskey Aged 7 Years",
    ],
    "STANDARD POURS": [
        "Latitude Beverage Portfolio - Wheel Horse & Copper & Cask",
        "James E. Pepper 'Decanter' Bourbon Barrel Proof",
        "James E. Pepper '1776' Bourbon 100pf",
        "James E. Pepper '1776' Rye 100pf",
        "Old Pepper Bottled in Bond Bourbon",
        "Pursuit United Triple Mash Bourbon (88 Proof)",
        "Pursuit United Triple Mash Rye (88Proof)",
        "Pursuit United Double Oaked Rye",
        "Pursuit United Double Oaked Bourbon",
        "Jimmy Red Classic Bourbon Whiskey",
        "Jimmy Red Bourbon Whiskey Bottled in Bond",
        "Jimmy Red Bourbon Whiskey Sherry Cask Finish",
        "Jimmy Red Bourbon Whiskey Double Oak",
        "Dingle Single Malt Irish Whiskey",
        "Hirsch - The Bivouac",
        "Arran 10 Year Single Malt Scotch Whisky",
        "Old Potrero 6 YR",
        "Nikka Coffey Grain",
        "Nikka FTB",
        "Starlight Blackberry Whiskey",
        "Starlight Peach Whiskey",
        "Starlight Carl T Bourbon",
        "Starlight Rickhouse Rye",
        "Bending Branch 1840 Kentucky Straight High Rye Bourbon",
        "ChickenDuck High Rye Bourbon",
        "ChickenDuck Wheated Bourbon",
        "ChickenDuck Four Grain Bourbon, Eclipse Edition",
        "Barrell Craft Spirits - Foundation 5 Year Bourbon",
        "Barrell Craft Spirits - Batch Series (Batch 037)",
        "Barrell Craft Spirits - Seagrass",
        "Barrell Craft Spirits - Black or Red Label TBD",
        "Boondocks 6 Year Straight 750ml",
        "Boondocks 6 Year Port 750ml",
        "Tomintoul Caribbean Rum Cask 750ml",
        "Tomintoul Cigar Malt 750ml",
        "Glencadam American Oak Highlands 750ml",
        "Glencadam 10 YR Highlands 750ml",
        "Brother's Bond Straight Bourbon Whiskey",
        "Brother's Bond American Rye Whiskey",
        "Brother's Bond Cask Strength Bourbon Whiskey",
        "Brother's Bond Bottled in Bond Bourbon Whiskey",
        "Brother's Bond Regenerative Grain",
        "Glengoyne (12/15/18)",
        "Tamdhu (12/15/18)",
        "Smokehead (Original/Terminado/15)",
        "Isle of Skye (21/25/30)",
        "Balcones Baby Blue",
        "Balcones Lineage",
        "Balcones Texas \"1\" Single Malt",
        "Balcones Rye Bottled-in-Bond",
        "Blue Note Juke Joint",
        "Blue Note Crossroads",
        "Blue Note Rye Whiskey",
        "Blue Note Uncut",
        "Tahwahkaro Distilling Company - Tah Four Grain Bourbon",
        "Tahwahkaro Distilling Company - Tah Four Grain Bourbon Cask Strength",
        "Tahwahkaro Distilling Company - Tah Rye Malt Whiskey",
        "Chicken Cock Kentucky Straight Bourbon",
        "Chicken Cock Wheated Kentucky Straight Bourbon",
        "Chicken Cock Kentucky Straight Rye",
        "Chicken Cock Double Oak 10 Year KY Whiskey",
        "Still Austin Cask Strength Bourbon",
        "Still Austin Cask Strength Rye",
        "Still Austin Single Barrel Bourbon",
        "Still Austin Single Barrel Rye",
        "Augusta KY Distillery - Old Route 8",
        "Augusta KY Distillery - Buckner's 10",
        "Augusta KY Distillery - Augusta Small Batch",
        "Augusta KY Distillery - Augusta Wheated Single Barrel",
        "Hooten Young Bottled-in-Bond Bourbon",
        "Hooten Young Rye Whiskey",
        "Hooten Young x Jack Carr Warrior Proof American Whiskey",
        "Hooten Young Barrel Proof American Whiskey – 15 YR",
        "Ole Smoky Salty Caramel Whiskey",
        "Ole Smoky Blackberry Whiskey",
        "Ole Smoky TN Straight Bourbon Whiskey",
        "Ole Smoky Salty Watermelon Whiskey",
        "Natterjack Irish Whiskey Blend No. 1",
        "Natterjack Irish Whiskey The Mistake",
        "Natterjack Irish Whiskey Cask Strength",
        "Horse Soldier Straight Bourbon",
        "Horse Soldier Small Batch Bourbon",
        "Horse Soldier Barrel Strength Bourbon",
        "American Metal Whiskey (V8)",
        "American Metal The Knuckle",
        "American Metal The Disciple",
        "St. George Spirits - Baller American Single Malt Whiskey",
        "El Dorado 8 Year Old Rum",
        "El Dorado 12 Year Old Rum",
        "El Dorado 15 Year Old Rum",
        "El Dorado 21 Year Old Rum",
        "Tanteo Jalapeno T",
    ],
}

all_drinks = [d for group in sections.values() for d in group]

# ---------- SESSION STATE ----------

if "checked" not in st.session_state:
    st.session_state.checked = {d: False for d in all_drinks}
if "notes" not in st.session_state:
    st.session_state.notes = {d: "" for d in all_drinks}
if "cigars" not in st.session_state:
    st.session_state.cigars = {d: "" for d in all_drinks}

# ---------- SIDEBAR SUMMARY ----------

st.sidebar.header("Progress")
total = len(all_drinks)
tried = sum(1 for d in all_drinks if st.session_state.checked[d])
percent = (tried / total * 100) if total else 0
st.sidebar.metric("Drinks tried", f"{tried} / {total}")
st.sidebar.progress(percent / 100.0)
st.sidebar.write(f"{percent:.1f}% complete")

search = st.sidebar.text_input("Search drinks")

# ---------- MAIN CONTENT ----------

for section_name, drinks in sections.items():
    st.subheader(section_name)

    for drink in drinks:
        if search and search.lower() not in drink.lower():
            continue

        with st.expander(drink, expanded=False):
            col1, col2 = st.columns([1, 3])

            with col1:
                st.session_state.checked[drink] = st.checkbox(
                    "Tried", value=st.session_state.checked[drink], key=f"check_{drink}"
                )

            with col2:
                st.markdown("**Notes**")
                st.session_state.notes[drink] = st.text_area(
                    "", value=st.session_state.notes[drink], key=f"notes_{drink}"
                )

                st.markdown("**Cigar Pairing**")
                st.session_state.cigars[drink] = st.text_area(
                    "", value=st.session_state.cigars[drink], key=f"cigar_{drink}"
                )

st.write("---")
st.write(
    "Tip: Add this page to your phone's home screen so it feels like an app. "
    "Each brother can open the link, use their own checklist, and keep their own notes."
)
