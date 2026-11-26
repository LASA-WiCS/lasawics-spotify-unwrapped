# lasawics-spotify-unwrapped
UNRELEASED! Check back soon :) 
- last update on 11/26

# LASA WiCS+ Spotify Unwrapped Workshop (Dec 7, 2026)

Decode Spotify Wrapped using real **Hashmap aggregation** and **custom sorting algorithms** on 10,000+ streaming logs, and generate your own custom Wrapped card!

## Quick Setup
1. Click the green **"USE THIS TEMPLATE"** button at the top right, then click **"Open in a codespace"**
2. Choose your language
   - **Java 21 (APCS Recc):** Open 'WrappedEngine.java' and complete TODO 1-3
   - **Python**: Open 'wrapped_engine.py' and complete TODO 1-3

## Running Code & Viewing Wrapped Card
- **Java**: Run 'javac WrappedEngine.java && java WrappedEngine' in the terminal
- **Python**: Run 'python3 wrapped_engine.py' in the terminal
- **VIEW UI**: Right click the 'my_wrapped.html' file --> **"Open with Live Server"** (or download/preview) and show to a WiCS Captain!

## Flags
1. **VALID MINUTES LISTENED:**: Spotify only counts a stream is 'ms_played>= 30,000' (30sec), so filter out skips and calculate total minutes listened
2. **TOP 5 Artists:** Use a hashmap or dictionary to aggregate total 'ms_played' per artist (valid streams only). Then, sort descending to rank the Top 5
3. **LONGEST BINGE (bonus):** Sort all streams chronologically by 'timestamp' and find the longest consecuitve streak of listening to the same artist
