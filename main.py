import json

def extract_usernames(input_file, output_file, key=None):
    """Extract usernames from Instagram JSON export and save in a simpler format."""
    with open(input_file, "r") as f:
        data = json.load(f)
    
    if key and key in data:
        data = data[key]  # Navigate to correct key for 'following.json'
    
    usernames = [entry["string_list_data"][0]["value"] for entry in data if "string_list_data" in entry]

    with open(output_file, "w") as f:
        json.dump(usernames, f, indent=4)
    
    print(f"Extracted {len(usernames)} usernames and saved to {output_file}.")

def load_usernames(filename):
    with open(filename, "r") as f:
        return json.load(f)

def find_unfollowers(followers, following):
    return list(set(following) - set(followers))

def find_nonfollowers(followers, following):
    return list(set(followers) - set(following))

def export_list(data, filename):
    """Export a list of usernames to a text file."""
    with open(filename, "w") as f:
        f.write("\n".join(data))
    print(f"Exported {len(data)} usernames to {filename}.")

def main():
    extract_usernames("followers.json", "followers_condensed.json")  # No key needed
    extract_usernames("following.json", "following_condensed.json", "relationships_following")  # Use correct key
    
    followers = load_usernames("followers_condensed.json")
    following = load_usernames("following_condensed.json")
    
    unfollowers = find_unfollowers(followers, following)
    nonfollowers = find_nonfollowers(followers, following)
    
    print(f"Loaded {len(followers)} followers and {len(following)} following accounts.")
    print("Unfollowers:", "None" if not unfollowers else "\n".join(unfollowers))
    print("Non-followers:", "None" if not nonfollowers else "\n".join(nonfollowers))
    
    # Export results to text files
    export_list(unfollowers, "unfollowers.txt")
    export_list(nonfollowers, "nonfollowers.txt")

if __name__ == "__main__":
    main()
