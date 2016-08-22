clear
rm *.pdf
python yahoo_test02.py
pdftk *.pdf cat output C20Stocks.pdf
python email_func.py
