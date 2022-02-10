description = '''
Simple API made possible by FastAPI.

## Tickers

You can **add or retrieve crypto-currency tickers**. 
\nExample: BTC-USD

## Historical Data

You can **add or retrieve cryptocurrency historical data**. 
You can retrieve such data for a specific date range and ticker. Supports day time-frame only.

## Database

You can **clear all cryptocurrency historical data and tickers**.
'''

tags_metadata = [
    {
        'name': 'Tickers',
        'description': 'Add or retrieve cryptocurrency tickers.'
    },
    {
        'name': 'Historical Data',
        'description': 'Add or retrieve cryptocurrency historical data.'
    },
    {
        'name': 'Database',
        'description': 'Clear all historical data and tickers.'
    }
]
