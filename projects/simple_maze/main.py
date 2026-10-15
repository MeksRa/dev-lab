import msvcrt
import os
import sys
import time

GAME_MAP = [
    "####################",
    "#....#.............#",
    "#.##.#.###.#######.#",
    "#.#....#.........#.#",
    "#.#.####.#######.#.#",
    "#........#.....#...#",
    "##########.###.###.#",
    "#........#.#.......#",
    "#.######.#.#.#####.#",
    "#.#......#...#.....X",
    "####################",
]

player_x, player_y = 1, 1


def draw_map():
    """Rendering the map without flickering"""
    # ansi-code '\x1b[H' -> Moving the cursor to the beginning(0,0) instead of 'cls' flickering
    # .write() -> print a new frame directly over the old one
    sys.stdout.write("\x1b[H")

    screen = []  # empty list where we will store the frame's rows.
    # Iterate through each row of the map (r is the row index, row is the row of text itself)
    for r, row in enumerate(GAME_MAP):
        row_chars = []  # List of characters for the current line
        # Iterate through each character in the string (c — column index, char — a character)
        for c, char in enumerate(row):
            if c == player_x and r == player_y:
                row_chars.append("P ")  # Player
            elif char == "#":
                row_chars.append("██")  # Wall
            elif char == ".":
                row_chars.append("· ")  # Empty space
            elif char == "X":
                row_chars.append("X ")  # Exit
        # Combine the string's characters into a single text string and add it to the main screen
        screen.append("".join(row_chars))
    screen.append("Controls: W/A/S/D — walk, Q — exit")
    # Output the entire assembled screen to the output stream with a single command
    sys.stdout.write("\n".join(screen) + "\n")
    # Forcefully flush the output buffer so that the text appears instantly
    sys.stdout.flush()


def get_key():
    """Reads a keypress in Windows without freezing"""
    if msvcrt.kbhit():
        try:
            return msvcrt.getch().decode("utf-8", errors="ignore").lower()
        except Exception:  # noqa: BLE001
            return None
    return None


def main() -> None:
    global player_x, player_y
    # Terminal initialization when the script starts:
    sys.stdout.write("\x1b[?25l")  # Hiding the blinking text cursor in the console
    os.system("cls")  # Clear the screen exactly once before the game starts
    try:
        while True:
            draw_map()  # We call our rendering function for the first time
            # Read a key
            key = get_key()
            if key == "q":
                break

            # Calculating potential new coordinates
            new_x, new_y = player_x, player_y
            if key == "w":
                new_y -= 1
            elif key == "s":
                new_y += 1
            elif key == "a":
                new_x -= 1
            elif key == "d":
                new_x += 1

            # Collision check (stay within bounds and don't walk into '#' walls)
            if 0 <= new_y < len(GAME_MAP) and 0 <= new_x < len(GAME_MAP[0]):
                target_cell = GAME_MAP[new_y][new_x]

                if target_cell != "#":  # If this is a passageway or an exit
                    player_x, player_y = new_x, new_y

                    # Step 4: Check for a win (if landing on the 'X' square)
                    if target_cell == "X":
                        os.system("cls")
                        print("VICTORY! You have escaped the labyrinth!")
                        break

            # A short pause to avoid loading the CPU to 100%
            time.sleep(0.03)

    except KeyboardInterrupt:
        pass
    finally:
        # Restore the cursor before exiting
        sys.stdout.write("\x1b[?25h\n")
        print("The game is over.")


if __name__ == "__main__":
    main()
