# GUI Database Project

Version: 1.0

This project is a Graphical User Interface (GUI) application for managing a database. The frontend of the application is written in PySide6, a Python binding for the Qt framework. The project follows the Model View/Controller (MVC) architecture to separate the concerns of data, presentation, and user interaction.

## Features

- User-friendly interface for interacting with the database.
- Support for various CRUD (Create, Read, Update, Delete) operations on the database records.
- Implementation of the MVC architecture for clear separation of responsibilities.
- Utilizes the fast retrieval capabilities of the MIT-licensed `btree.c` backend.

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.x
- PySide6 library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Install the required Python dependencies:
  ```bash
  pip install PySide6
  ```
3. Compile and install the btree.c backend:
   ```bash
   gcc -o btree btree.c
   ```
## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your forked repository.
- Submit a pull request detailing your changes.
## License
The btree.c backend is licensed under the MIT License. See the ***btree.c LICENSE*** file for more information.

The frontend code and GUI application are licensed under the ***MIT License***. See the LICENSE file for more information.
