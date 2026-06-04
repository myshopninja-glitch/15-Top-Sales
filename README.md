## ⚙️ Data Pipeline & Synchronization

To optimize performance and bypass aggressive e-commerce rate limits during personal research, the application utilizes an automated server-side caching layer:

- **Refresh Interval:** Every 3 hours (`ttl=10800` seconds).
- **Behavior:** The dashboard holds data in an volatile memory cache. The very first page ping after a 3-hour window expires forces the data matrix to discard legacy entries and execute a clean crawl/refresh across Amazon, Etsy, AliExpress, and TikTok Shop.
- **State Preservation:** User-selected interactive UI components (like the active Chrono Vector day filter) remain stable across minor cache validations.
