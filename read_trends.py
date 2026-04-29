def generate_briefing(filename):
    print("--- DAILY AI TRENDS BRIEFING ---")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            # Skip the header and table formatting lines
            for line in lines[4:]: 
                if '|' in line:
                    columns = line.split('|')
                    name = columns[1].strip()
                    desc = columns[2].strip()
                    print(f"Project: {name}")
                    print(f"Summary: {desc}")
                    print("-" * 30)
    except FileNotFoundError:
        print("AITrends.md not found. Run the fetcher first!")

if __name__ == "__main__":
    generate_briefing("AITrends.md")
