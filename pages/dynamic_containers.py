from datetime import datetime

import pandas as pd
import streamlit as st


def remember_event(label: str, key: str) -> None:
    is_open = bool(st.session_state.get(key, False))
    state = "opened" if is_open else "closed"
    timestamp = datetime.now().strftime("%H:%M:%S")
    history = st.session_state.setdefault("event_history", [])
    history.insert(0, f"{timestamp}  {label} {state}")
    st.session_state.event_history = history[:8]


def toggle(key: str) -> None:
    st.session_state[key] = not bool(st.session_state.get(key, False))


st.title("Dynamic Containers")
st.caption("1.55.0 では expander と popover が open/close を state として扱えます。")

expander_col, popover_col = st.columns(2)

with expander_col:
    st.subheader("Expander reruns on open/close")
    st.button(
        "Toggle expander programmatically",
        on_click=toggle,
        args=("lazy_expander",),
        use_container_width=True,
    )
    summary = st.expander(
        "Open the lazy expander",
        icon=":material/unfold_more:",
        key="lazy_expander",
        on_change=remember_event,
        args=("Expander", "lazy_expander"),
    )
    with summary:
        if summary.open:
            chart_data = pd.DataFrame(
                {
                    "requests": [12, 18, 26, 31, 42, 48],
                    "errors": [1, 1, 2, 1, 1, 0],
                }
            )
            st.success(f"Rendered only while open at {datetime.now().strftime('%H:%M:%S')}.")
            st.line_chart(chart_data)
        else:
            st.info("Open this expander to trigger a rerun and render the chart.")

    st.write("expander.open", summary.open)

with popover_col:
    st.subheader("Popover reruns on open/close")
    st.button(
        "Open or close popover",
        on_click=toggle,
        args=("release_popover",),
        use_container_width=True,
    )
    drawer = st.popover(
        "Open release popover",
        icon=":material/filter_alt:",
        key="release_popover",
        on_change=remember_event,
        args=("Popover", "release_popover"),
        width="stretch",
    )
    with drawer:
        if drawer.open:
            st.write("This content is evaluated when the popover is open.")
            st.radio(
                "Which 1.55.0 feature is easiest to demo?",
                options=["Widget binding", "Dynamic containers", "Hidden pages"],
                horizontal=True,
                key="favorite_feature",
            )
            st.button("Close this popover", on_click=toggle, args=("release_popover",))
        else:
            st.write("Use the button above or the popover trigger to open this panel.")

    st.write("popover.open", drawer.open)

st.divider()

st.subheader("Interaction log")
for item in st.session_state.get("event_history", []):
    st.write(item)

if not st.session_state.get("event_history"):
    st.info("Open or close the expander and popover to see the event log update.")