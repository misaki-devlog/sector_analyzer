import streamlit as st
st.title("企業データ入力ツール（試作01）")
industry=st.selectbox(
    "1. 調べたい企業の業界を選択してください",
    ["選択してください","電機・電子機器","化学","食品","アパレル・繊維"]
)
st.divider()
if industry=="選択してください":
    st.info("業界を選択すると、入力欄が表示されます。")
elif industry=="電機・電子機器":
    st.subheader(f"【{industry}】の指標入力")
    operating_margin=st.number_input("営業利益率(%)",value=0.0,step=0.1)
    capex=st.number_input("設備投資費(100万)",value=0.0,step=0.1)
    r_and_d_expenses=st.number_input("研究開発費(100万)",value=0.0,step=0.1)
    if st.button("この内容で判定する"):
        st.success("(ここに将来、電機・電子機器業界の基準値を使った計算結果を表示します)")
        st.write(f"入力されたデータ-> 営業利益率:{operating_margin}%,設備投資費:{capex},研究開発費:{r_and_d_expenses}")
elif industry=="化学":
    st.subheader(f"【{industry}】の指標入力")
    operating_margin=st.number_input("営業利益率(%)",value=0.0,step=0.1)
    overseas_sales_ratio=st.number_input("海外売上比率(%)",value=0.0,step=0.1)
    r_and_d_expenses=st.number_input("研究開発費(100万)",value=0.0,step=0.1)
    if st.button("この内容で判定する"):
        st.success("(ここに将来、化学業界の基準値を使った計算結果を表示します)")
        st.write(f"入力されたデータ-> 営業利益率:{operating_margin},海外売上比率:{overseas_sales_ratio},研究開発費:{r_and_d_expenses}")

elif industry=="食品":
    st.subheader(f"【{industry}】の指標入力")
    operating_margin=st.number_input("営業利益率(%)",value=0.0,step=0.1)
    roe=st.number_input("ROE(%)",value=0.0,step=0.1)
    equity_ratio=st.number_input("自己資本比率(%)",value=0.0,step=0.1)
    if st.button("この内容で判定する"):
        st.success("(ここに将来、食品業界の基準値を使った計算結果を表示します)")
        st.write(f"入力されたデータ-> 営業利益率:{operating_margin},ROE:{roe},自己資本比率:{equity_ratio}")

elif industry=="アパレル・繊維":
    st.subheader(f"【{industry}】の指標入力")
    operating_margin=st.number_input("営業利益率(%)",value=0.0,step=0.1)
    capex=st.number_input("設備投資費(100万)",value=0.0,step=0.1)
    overseas_sales_ratio=st.number_input("海外売上比率(%)",value=0.0,step=0.1)
    if st.button("この内容で判定する"):
        st.success("(ここに将来、アパレル・繊維業界の基準値を使った計算結果を表示します)")
        st.write(f"入力されたデータ-> 営業利益率:{operating_margin},設備投資費:{capex},海外売上比率:{overseas_sales_ratio}")
        