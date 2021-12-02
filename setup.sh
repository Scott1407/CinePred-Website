mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
 \n\
[theme]\n\
primaryColor=#3872fb\n\
backgroundColor=#0e1117\n\
secondaryBackgroundColor=#cece1b\n\
textColor=#fafafa\n\
" > ~/.streamlit/config.toml
