import streamlit as st
import json
import time
import re

from backend.streamlitsettings  import _max_width_
_max_width_(st.sidebar.slider('屏幕比例', 30, 100, 75))

st.title('Regexp')

st.markdown('查看：<a href="https://tool.oschina.net/uploads/apidocs/jquery/regexp.html">正则表达式全集</a>', unsafe_allow_html=True);

features = [
    '基本正则'
]

feature = st.sidebar.selectbox('选择', options=features)
if feature == '基本正则':
    
    flags = {
        'ASCII':                   re.RegexFlag.ASCII,
        '忽略大小写(IGNORECASE)':   re.RegexFlag.IGNORECASE,
        '本地化(LOCALE)':          re.RegexFlag.LOCALE,
        'Unicode(UNICODE)':       re.RegexFlag.UNICODE,
        '多行模式(MULTILINE)':     re.RegexFlag.MULTILINE,
        '点号匹配所有字符(DOTALL)': re.RegexFlag.DOTALL,
        '详细模式(VERBOSE)':       re.RegexFlag.VERBOSE,
    }    

    res = st.text_input('输入表达式')
    flag = st.selectbox('选择 flags', options=flags.keys())
    text = st.text_area('输入比较内容')
    st.button('比较', use_container_width=True)
    
    rescomile = re.compile(res, flags=flags[flag])
    
    st.text_input(f'match', rescomile.match(text))
    matchs = []
    index = 0
    while True:
        match = rescomile.match(text[index:])
        print('比较', time.time(), match)
        if match == None:
            break
        if match.start() == match.start():
            break
        index += match.end()
        matchs.append(match.group())
    st.text_input(f'matchs - {len(matchs)}', matchs)
    
    # st.text_input(f'match', rescomile.match(text))
    st.text_input('fullmatch', rescomile.fullmatch(text))
    st.text_input('findall', rescomile.findall(text))
    if rescomile.search(text):
        # st.text_input('search', rescomile.search(text))
        # st.text_input('search - group(1)', rescomile.search(text).group(1))
        
        col1, col2 = st.columns(2)
        with col1:
            
            st.text_input('search', rescomile.search(text).group(0))
        
        with col2:
            for i, v in enumerate(rescomile.search(text).groups()):
                st.text_input(f'search - group({i})', rescomile.search(text).group(i))
        
        # groups = {}
        # for i, v in enumerate(rescomile.search(text).groups()):
        #     groups[f'{i}'] = str(v)
        # st.table(groups)
    subs = st.text_input('sub - input')
    replaced = st.text_area('sub - output', rescomile.sub(subs, text))
    # st.text_area('search', rescomile.search(text))
    try:
        dict = {}
        for i in json.loads(replaced):
            dict[i] = i
        st.text_input('unique', dict.keys())
    except:
        st.warning('not unique')