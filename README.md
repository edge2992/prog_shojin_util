# prog_shojin_util: Competitive Programming Problem Fetcher

[![PyPI version](https://badge.fury.io/py/prog-shojin-util.svg)](https://badge.fury.io/py/prog-shojin-util)
[![Unit Test](https://github.com/edge2992/prog_shojin_util/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/edge2992/prog_shojin_util/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/edge2992/prog_shojin_util/branch/main/graph/badge.svg?token=74WPEN5WLV)](https://codecov.io/gh/edge2992/prog_shojin_util)

Fetch and organize competitive programming problems from various blogs with ease.

## Table of Contents

- [prog\_shojin\_util: Competitive Programming Problem Fetcher](#prog_shojin_util-competitive-programming-problem-fetcher)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
    - [Integration with atcoder-cli](#integration-with-atcoder-cli)
  - [Supported Contest Platforms](#supported-contest-platforms)
  - [Installation](#installation)
    - [Examples](#examples)
  - [Options](#options)
  - [Acknowledgements](#acknowledgements)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

`prog-shojin-util` (pshu) is a CLI utility tool tailored to extract competitive programming problems not directly from contest platforms, but from blogs and websites that curate high-quality problems, particularly from renowned platforms like AtCoder and Yukicoder. By sifting through these selected compilations, users can focus on problems that are recommended by the community, filtering them based on criteria like AC status, date range, and more.

## Features

- **User-Based Filtering**: Focus on problems based on a specific user's activity on platforms like AtCoder.
- **Problem Status Filtering**: Whether you're looking to find unsolved problems or revisit those you've already solved, `prog_shojin_util` has you covered.
- **Flexible Output**: Obtain your results in various formats such as JSON, Markdown, CSV, and more.
- **Date-based Retrieval**: Fetch problems available since a specific date for targeted practice sessions.

### Integration with atcoder-cli

`prog_shojin_util` offers integration capabilities with [`atcoder-cli`](https://github.com/Tatamo/atcoder-cli), an essential tool in the competitive programming community. By saving the fetched problems as `contest.acc.json` in a directory and then using `atcoder-cli` in that directory, you can streamline your problem-solving workflow.

1. **Create a Workspace for Practice**:
   Begin by setting up a designated workspace for the problems.

   ```bash
   mkdir practice
   cd practice
   ```

2. **Fetch Unsolved Problems with prog_shojin_util**:
   Fetch problems curated by a specific user (`edge2992` in this case) from a Qiita post and save them in a format suitable for `atcoder-cli`.

   ```bash
    pshu --atcoder-user edge2992 \
         -t https://qiita.com/e869120/items/f1c6f98364d1443148b3 \
         --status not-ac \
         --output acc_json > contest.acc.json
   ```

3. **Integrate with atcoder-cli**:
   With the `contest.acc.json` file at hand, you can now use the `atcoder-cli` to add the problems to your list of tasks.

   ```bash
   acc add -c inquire
   ```

By following these steps, you can efficiently extract unsolved problems from a curated list, then download and submit tests using atcoder-cli.

## Supported Contest Platforms

Here's a list of contest platforms supported by `prog_shojin_util`:

| Contest Platform  | Support Status |
| ----------------- | -------------- |
| AtCoder           | ✅              |
| Yukicoder         | ✅              |
| [Other platforms] | ❌              |

## Installation

To install `prog_shojin_util`, use the following command:

```bash
pip install prog_shojin_util
```

Ensure you have a compatible Python version installed.

### Examples

To fetch unsolved problems from a specific URL for a given AtCoder user:

```bash
pshu --atcoder-user john_doe \
     -t https://example.com/problems \
     --status not-ac
```

To obtain all problems in CSV format for a Yukicoder user:

```bash
pshu --yukicoder-user jane_doe \
     -t https://example.com/problems \
     --status both --output csv
```

For detailed options and configurations, consult the [Options](#options) section.

## Options

Here's a breakdown of the available options in `prog_shojin_util`:

- `--atcoder-user TEXT`: Specify the User ID for AtCoder to filter problems based on the user's activity.

- `--yukicoder-user TEXT`: Specify the User Name for Yukicoder to filter problems based on the user's activity.

- `-t, --target TEXT`: The base URL from which problem links will be fetched. This option is mandatory.

- `--status [ac|not-ac|both]`: Filter problems based on their AC (Accepted) status.
  - `ac`: For problems already solved.
  - `not-ac`: For unsolved problems.
  - `both`: For all problems. The default is `not-ac`.

- `--output [json|markdown|csv|acc_json]`: Choose the desired output format:
  - `json`: Standard JSON format.
  - `markdown`: Markdown format.
  - `csv`: CSV format.
  - `acc_json`: The format used by the atcoder-cli tool. The default is `json`.

- `--since DATE_FORMAT`: Filter problems available since the specified date. Use the format 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'. The default is set to 2012-01-01.

- `--verbose`: Enable this option for detailed logging, which aids in debugging.

For command-line help, use the `--help` option.

## Acknowledgements

Special thanks to the [AtCoder Problems API](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md) and [Yukicoder API](https://petstore.swagger.io/?url=https://yukicoder.me/api/swagger.yaml) for providing invaluable data resources. Our tool, `prog_shojin_util`, greatly benefits from its capabilities.

## Contributing

If you'd like to contribute to the project, feel free to submit issues or pull requests.

## License

MIT
