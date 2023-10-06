# Hacker Typer

Hacker Typer is a Python script that simulates a hacker typing out a desired string with various effects, including random characters and "casino letters" that change before getting fixed. It's a fun and entertaining way to display text as if it's being typed by a hacker in a terminal.

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Parameters](#parameters)
- [Examples](#examples)

## Getting Started

To use Hacker Typer, follow these steps:

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the directory where the script is located.

## Usage

To use the script, you'll need to import it into your Python environment and call the `hackerPrint` function with the desired parameters. Additionally, you can follow these instructions for running the script in the command prompt (cmd):

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located using the `cd` command. For example:

   ```
   cd path/to/script/directory
   ```

4. Start a Python session by typing `python` in the command prompt.

5. Import the `main` module:

   ```python
   import main
   ```

6. Use the `main.hackerPrint` function with your desired parameters. For example:

   ```python
   main.hackerPrint('Hello World', 3, 0.01, True, 100, 5)
   ```

This will execute the Hacker Typer script with the specified parameters, and you'll see the hacker-like typing effect in your command prompt. The script will type out the desired text with random characters and casino letters.

Feel free to customize the parameters as needed to achieve the desired typing effect. Enjoy using Hacker Typer to create entertaining terminal-like displays!

## Parameters

The `hackerPrint` function takes the following parameters:

1. `desired_text` (str): The text you want the hacker to type out.
2. `max_chars` (int): The maximum number of characters to display before writing the next letter.
3. `delay` (float): The time delay (in seconds) between each iteration (usually a small value, e.g., 0.01 for 10 milliseconds).
4. `clear_terminal` (bool): Whether to clear the terminal between each iteration (compatible with macOS, Linux, and Windows).
5. `casino_letters_amount` (int): The percentage of letters that keep going random after the next letter is fixed (0 to 100%).
6. `casino_duration` (int): How long "casino letters" need to roll before getting fixed.

## Examples

Here are some example usages of the `hackerPrint` function:

```python
# Basic usage
main.hackerPrint('Hello World')

# With custom parameters
main.hackerPrint('Hack the Planet!', 2, 0.05, False, 50, 3)
```

Feel free to customize the parameters to achieve the desired typing effect.

Enjoy using Hacker Typer to create entertaining terminal-like displays!
