# prog_shojin_util

## Introduction

`prog-shojin-util` is a CLI utility tool designed to fetch competitive programming problems from popular platforms like AtCoder and Yukicoder. The tool allows users to filter problems based on various criteria such as AC status, date range, and more.

## Features

1. **Support for Multiple Platforms:** Currently supports fetching problems from AtCoder and Yukicoder.
2. **Filtering by AC Status:** Filter problems based on their AC (Accepted) status.
3. **Flexible Date Filtering:** Specify a date to filter problems that were available since that particular date.
4. **User-Based Filtering:** Provide user IDs for specific platforms to get problems relevant to their activity.
5. **Multiple Output Formats:** Choose between JSON, Markdown, or CSV formats for output.

## Installation

Ensure you have Python and Poetry installed on your system.

```bash
# Clone the repository
git clone https://github.com/your-github-username/prog-shojin-util.git

# Navigate to the directory
cd prog-shojin-util

# Install the package using Poetry
poetry install
```

## Usage

To use the CLI tool, run:

```bash
poetry run prog-shojin-util [OPTIONS]
```

### Options

- `--atcoder-user TEXT`: Specify the User ID for AtCoder to filter problems based on user activity.
- `--yukicoder-user TEXT`: Specify the User Name for Yukicoder to filter problems based on user activity.
- `-t, --target TEXT`: The base URL from which problem links will be collected. This option is required.
- `--status [ac|not-ac|both]`: Choose the AC status to filter problems. Options are 'ac' for solved problems, 'not-ac' for unsolved problems, and 'both' for all problems. Default is 'not-ac'.
- `--output [json|markdown|csv]`: Select the desired output format. Available formats are JSON, Markdown, and CSV. Default is JSON.
- `--since DATE`: Filter problems that were available since the specified date. The default is set to '2012-01-01', which is the starting date for AtCoder.
- `--verbose`: Enable this option for detailed logging, useful for debugging.

### Examples

To fetch unsolved problems from a specific URL for a given AtCoder user:

```bash
poetry run prog-shojin-util --atcoder-user john_doe -t https://example.com/problems --status not-ac
```

To get all problems in CSV format for a Yukicoder user:

```bash
poetry run prog-shojin-util --yukicoder-user jane_doe -t https://example.com/problems --status both --output csv
```

## Contributing

Feel free to raise issues or pull requests if you want to contribute to the project.

## License

MIT
