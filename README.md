# Instagram Unfollowers Tracker

This Python script helps you track who unfollowed you on Instagram and who doesn't follow you back.

## Features
- Extracts usernames from Instagram JSON data exports
- Identifies users who unfollowed you
- Finds users you follow who don't follow you back
- Exports results to text files

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/dbar2002/IG-Follower-Tool
   cd instagram-unfollowers-tracker
   ```

2. **Set Up a Virtual Environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies** (if needed)
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Download Your Instagram Data:**
   - Go to Instagram settings > "Your Activity" > "Download Your Information"
   - Extract the ZIP file and find `followers.json` and `following.json`

2. **Run the Script:**
   ```sh
   python main.py
   ```

3. **View the Results:**
   - `unfollowers.txt` → List of users who unfollowed you
   - `nonfollowers.txt` → List of users you follow who don’t follow back

## File Structure
```
instagram-unfollowers-tracker/
│── followers.json              # Instagram exported followers list
│── following.json              # Instagram exported following list
│── main.py                     # Main script
│── requirements.txt             # Dependencies (if any)
│── .gitignore                   # Ignored files
│── README.md                    # Project documentation
```

## Contributing
Feel free to submit pull requests or report issues!

## License
This project is licensed under the MIT License.
