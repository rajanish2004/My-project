import sys
import pyfiglet
import random

# List of supported fonts available in pyfiglet
SUPPORTED_FONTS = pyfiglet.FigletFont.getFonts()

def print_usage_and_exit():
    print("Invalid Usage")
    sys.exit(1)

def main():
    if len(sys.argv) == 1:
        # No arguments provided, use a random font
        selected_font = random.choice(SUPPORTED_FONTS)
        text = input("Enter text to convert into ASCII art: ")
    elif len(sys.argv) == 3:
        # Two arguments expected: -f or --font FONT_NAME
        if sys.argv[1] in ['-f', '--font']:
            font_name = sys.argv[2]
            if font_name in SUPPORTED_FONTS:
                selected_font = font_name
                text = input("Enter text to convert into ASCII art: ")
            else:
                print(f"Error: Font '{font_name}' is not supported.")
                sys.exit(1)
        else:
            print_usage_and_exit()
    else:
        print_usage_and_exit()

    # Generate ASCII art
    ascii_art = pyfiglet.figlet_format(text, font=selected_font)
    print(ascii_art)

if __name__ == "__main__":
    main()
