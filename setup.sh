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
" > ~/.streamlit/config.toml

echo "\
[theme]\n\
primaryColor=#3872fb\n\
backgroundColor=#0e1117\n\
secondaryBackgroundColor=#cece1b\n\
textColor=#fafafa\n\
font=sans serif\n\
" > ~/.streamlit/config.toml
